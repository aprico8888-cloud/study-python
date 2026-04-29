alert("Welcome to my site!");

function hello() {
  alert("押された！");
}

function changeText() {
  document.getElementById("msg").textContent = "ようこそ";
}

document.getElementById("btn").addEventListener("click", () => {
  alert("押された！");
});