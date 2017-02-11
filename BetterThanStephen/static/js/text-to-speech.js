var synth = window.speechSynthesis;

var inputForm = document.querySelector('form');
var inputTxt = document.querySelector('.txt');
var voiceSelect = document.querySelector('select');

var pitch = document.querySelector('#pitch');
var pitchValue = document.querySelector('.pitch-value');
var rate = document.querySelector('#rate');
var rateValue = document.querySelector('.rate-value');

var voices = [];

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

		option.setAttribute('data-lang', voices[i].lang);
		option.setAttribute('data-name', voices[i].name);
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
	utterThis.pitch = pitch.value;
	utterThis.rate = rate.value;
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

document.getElementById("submit-button").onclick = function(){
	event.preventDefault();
	speak(inputTxt.value);
}

inputForm.onsubmit = function(event) {
	event.preventDefault();
	speak(inputTxt.value);
}

pitch.onchange = function() {
	pitchValue.textContent = pitch.value;
}

rate.onchange = function() {
	rateValue.textContent = rate.value;
}

