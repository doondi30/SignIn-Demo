function togglePassword() {
  const passwordInput = document.getElementById("password");
  const type = passwordInput.type === "password" ? "text" : "password";
  passwordInput.type = type;
}

document.getElementById("loginForm")?.addEventListener("submit", function (e) {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

// document.getElementById("loginForm").addEventListen("submit", function (e) {
//   const email = document.getElementById("email").value;
//   const password = document.getElementById("password").value;

  if (!email || !password) {
    alert("Please fill in both fields.");
    e.preventDefault();
  }
});

document.getElementById("signupForm")?.addEventListener("submit", function (e) {
  const email = document.getElementById("signup-email").value;
  if (!email) {
    alert("Please enter your email.");
    e.preventDefault();
  }
});
