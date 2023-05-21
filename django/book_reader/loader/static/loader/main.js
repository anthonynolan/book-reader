const doc = document.documentElement;
const events = [];
doc.addEventListener("click", (e) => {
  events.push(e);
  console.log("test" + e);
});
