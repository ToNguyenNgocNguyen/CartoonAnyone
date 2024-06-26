// Get the form and select element
const form = document.getElementById('language-form');
const select = document.getElementById('language-select');

// Add event listener to the select element
select.addEventListener('change', function() {
    // Submit the form when the select value changes
    form.submit();
});


function validateAndMove(input) {
    // Ensure only numbers are entered
    input.value = input.value.replace(/[^0-9]/g, '');
    
    // Move to next input field if current field is filled
    if (input.value.length === 1) {
        var nextInput = input.parentElement.nextElementSibling.querySelector('input');
        if (nextInput !== null) {
            nextInput.focus();
        }
    }
}

function moveBackward(input, event) {
    // Move to previous input field if backspace is pressed and current field is empty
    if (event.keyCode === 8 && input.value.length === 0) {
        var prevInput = input.parentElement.previousElementSibling.querySelector('input');
        if (prevInput !== null) {
            prevInput.focus();
        }
    }
}