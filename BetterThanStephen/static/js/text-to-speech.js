var synth = window.speechSynthesis;

var inputForm = document.getElementById("input-form");
var inputTxt = document.getElementById("input-text");
var voiceSelect = document.getElementById("language-select");

var voices = [];

function speakPayments() {
    setTimeout(function() {
        voiceSelect.selectedIndex = 2;
        var payments = document.getElementsByClassName("payment-entry");
        for (var i = 0, len = payments.length; i < len; i++) {
            //console.log(payments[i].innerText);
            //populateVoiceList();
            speak(payments[i].innerText);
        }
    }, 500);
}

function populateVoiceList() {
	voices = synth.getVoices();
	var selectedIndex = voiceSelect.selectedIndex < 0 ? 0 : voiceSelect.selectedIndex;
	voiceSelect.innerHTML = '';
	for(i = 0; i < voices.length ; i++) {
		var option = document.createElement('option');
		option.textContent = voices[i].name + ' (' + voices[i].lang + ')';

		if(voices[i].default) {
		  	option.textContent += ' -- DEFAULT';
		}

		option.setAttribute('data-lang', 'en-GB');
		// option.setAttribute('data-name', voices[i].name);
		voiceSelect.appendChild(option);
	}
	voiceSelect.selectedIndex = selectedIndex;
}

function speak(text) {
	var utterThis = new SpeechSynthesisUtterance(text);
	var selectedOption = voiceSelect.selectedOptions[0].getAttribute('data-name');
	for(i = 0; i < voices.length ; i++) {
		if(voices[i].name === selectedOption) {
  			utterThis.voice = voices[i];
		}
	}
	utterThis.pitch = 1;
	utterThis.rate = 1;
	synth.speak(utterThis);

	utterThis.onpause = function(event) {
		var char = event.utterance.text.charAt(event.charIndex);
		console.log('Speech paused at character ' + event.charIndex + ' of "' +
		event.utterance.text + '", which is "' + char + '".');
	}
}

populateVoiceList();
if (speechSynthesis.onvoiceschanged !== undefined) {
	speechSynthesis.onvoiceschanged = populateVoiceList;
}

document.getElementById("talk-button").onclick = function(){
	event.preventDefault();
	speak(inputTxt.value);
}

speakPayments();
