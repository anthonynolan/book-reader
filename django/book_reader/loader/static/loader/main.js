const doc = document.documentElement;
const events = [];

const eventHappened = (e) => {
  events.push({ date: Date.now(), type: e.type, target: e.target });
};

doc.addEventListener("click", (e) => {
  eventHappened(e);
});
