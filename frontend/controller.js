$(document).ready(function () {
  // Display Speak Message
  eel.expose(DisplayMessage);
  function DisplayMessage(message) {
    var siriMessageElement = $(".siri-message li:first");
    if (siriMessageElement.length) {
      siriMessageElement.text(message);
      $(".siri-message").textillate("start");
    } else {
      console.error('Element with class "siri-message li:first" not found.');
    }
  }

  eel.expose(ShowHood);
  function ShowHood() {
    var ovalElement = $("#Oval");
    var siriWaveElement = $("#SiriWave");
    if (ovalElement.length && siriWaveElement.length) {
      ovalElement.attr("hidden", false);
      siriWaveElement.attr("hidden", true);
    } else {
      console.error('Elements with IDs "Oval" and/or "SiriWave" not found.');
    }
  }

  eel.expose(senderText);
  function senderText(message) {
    var chatBox = document.getElementById("chat-canvas-body");
    if (chatBox && message.trim() !== "") {
      chatBox.innerHTML += `<div class="row justify-content-end mb-4">
          <div class="width-size">
          <div class="sender_message">${message}</div>
          </div>
      </div>`;

      // Scroll to the bottom of the chat box
      chatBox.scrollTop = chatBox.scrollHeight;
    } else {
      console.error('Element with ID "chat-canvas-body" not found or message is empty.');
    }
  }

  eel.expose(receiverText);
  function receiverText(message) {
    var chatBox = document.getElementById("chat-canvas-body");
    if (chatBox && message.trim() !== "") {
      chatBox.innerHTML += `<div class="row justify-content-start mb-4">
          <div class="width-size">
          <div class="receiver_message">${message}</div>
          </div>
      </div>`;

      // Scroll to the bottom of the chat box
      chatBox.scrollTop = chatBox.scrollHeight;
    } else {
      console.error('Element with ID "chat-canvas-body" not found or message is empty.');
    }
  }

  eel.expose(hideLoader);
  function hideLoader() {
    var loaderElement = $("#Loader");
    var faceAuthElement = $("#FaceAuth");
    if (loaderElement.length && faceAuthElement.length) {
      loaderElement.attr("hidden", true);
      faceAuthElement.attr("hidden", false);
    } else {
      console.error('Elements with IDs "Loader" and/or "FaceAuth" not found.');
    }
  }

  // Hide Face auth and display Face Auth success animation
  eel.expose(hideFaceAuth);
  function hideFaceAuth() {
    var faceAuthElement = $("#FaceAuth");
    var faceAuthSuccessElement = $("#FaceAuthSuccess");
    if (faceAuthElement.length && faceAuthSuccessElement.length) {
      faceAuthElement.attr("hidden", true);
      faceAuthSuccessElement.attr("hidden", false);
    } else {
      console.error('Elements with IDs "FaceAuth" and/or "FaceAuthSuccess" not found.');
    }
  }

  // Hide success and display
  eel.expose(hideFaceAuthSuccess);
  function hideFaceAuthSuccess() {
    var faceAuthSuccessElement = $("#FaceAuthSuccess");
    var helloGreetElement = $("#HelloGreet");
    if (faceAuthSuccessElement.length && helloGreetElement.length) {
      faceAuthSuccessElement.attr("hidden", true);
      helloGreetElement.attr("hidden", false);
    } else {
      console.error('Elements with IDs "FaceAuthSuccess" and/or "HelloGreet" not found.');
    }
  }

  // Hide Start Page and display blob
  eel.expose(hideStart);
  function hideStart() {
    var startElement = $("#Start");
    var ovalElement = $("#Oval");
    if (startElement.length && ovalElement.length) {
      startElement.attr("hidden", true);

      setTimeout(function () {
        ovalElement.addClass("animate__animated animate__zoomIn");
      }, 1000);
      setTimeout(function () {
        ovalElement.attr("hidden", false);
      }, 1000);
    } else {
      console.error('Elements with IDs "Start" and/or "Oval" not found.');
    }
  }
});
