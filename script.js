let ipaDict = {};

// Load IPA dictionary from JSON file
fetch("ipa_dictionary.json")
    .then(response => response.json())
    .then(data => ipaDict = data)
    .catch(error => console.error("Error loading IPA dictionary:", error));

function convert() {
    let text = document.getElementById("inputText").value.trim().toLowerCase();
    let accent = document.getElementById("accent").value;
    let words = text.split(/\s+/); // Tách câu thành từng từ
    let resultWords = [];

    words.forEach(word => {
        if (ipaDict[word]) {
            // Chuyển từ Anh → IPA
            resultWords.push(ipaDict[word][accent] || word);
        } else {
            // Chuyển từ IPA → Anh
            let foundWord = Object.keys(ipaDict).find(key => ipaDict[key][accent] === word);
            resultWords.push(foundWord || word);
        }
    });

    document.getElementById("outputText").value = resultWords.join(" ");
}
