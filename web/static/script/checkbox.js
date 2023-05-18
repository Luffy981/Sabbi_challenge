document.addEventListener('DOMContentLoaded', function() {
  var questionContainers = document.querySelectorAll('.form-group');

  questionContainers.forEach(function(container) {
    var checkboxes = container.querySelectorAll('input[type="checkbox"]');

    checkboxes.forEach(function(checkbox) {
      checkbox.addEventListener('change', function() {
        if (this.checked) {
          checkboxes.forEach(function(otherCheckbox) {
            if (otherCheckbox !== checkbox) {
              otherCheckbox.disabled = true;
            }
          });
        } else {
          checkboxes.forEach(function(otherCheckbox) {
            if (otherCheckbox !== checkbox) {
              otherCheckbox.disabled = false;
            }
          });
        }
      });
    });
  });
});
