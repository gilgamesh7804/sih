document.getElementById('send-otp').addEventListener('click', function (e) {
    e.preventDefault();
    const email = document.getElementById('email-phone').value;
  
    // Send OTP request
    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email })
    })
    .then(response => response.json())
    .then(data => {
      if (data.message) {
        window.location.href="http://127.0.0.1:5000/login2";
      } else {
        alert("DIDN'T");
      }
    })
    .catch(error => console.error('Error:', error));
  });
  
  