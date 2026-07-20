
// Bootstrap validation
(function () {
  'use strict'
  var form = document.getElementById('demoForm')
  form.addEventListener('submit', function (event) {
    if (!form.checkValidity()) {
      event.preventDefault()
      event.stopPropagation()
    } else {
      event.preventDefault();
      alert('Demo request submitted successfully!');
      // Optional: submit via AJAX here
      form.reset();
      var modal = bootstrap.Modal.getInstance(document.getElementById('demoModal'))
      modal.hide();
    }
    form.classList.add('was-validated')
  }, false)
})();



function scrollLeft() {
    const container = document.getElementById("scrollContainer");
    container.scrollBy({
        left: -320,
        behavior: "smooth"
    });
}

function scrollRight() {
    const container = document.getElementById("scrollContainer");
    container.scrollBy({
        left: 320,
        behavior: "smooth"
    });
}


