document.addEventListener("DOMContentLoaded", function () {
  var count = 0;
  var button = document.getElementById("counterButton");
  var counterDisplay = document.getElementById("clickCount");

  button.addEventListener("click", function () {
    count++;
    counterDisplay.innerText = count;
  });
});
