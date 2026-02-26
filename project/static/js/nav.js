let toggleBtn = document.getElementById("navbar-toggle");
let collapse = document.getElementById("navbar-collapse");
console.log(toggleBtn);

toggleBtn.onclick = () => {
  collapse.classList.toggle("hidden");
  collapse.classList.toggle("flex");
};
