function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function buildingstoRoom(buildingName){
  fetch("/Dashboard/Building/go-to-rooms", {
    method: "POST",
    body: JSON.stringify({ buildingName: buildingName }),
  }).then((_res) => {
    window.location.href = "/Dashboard/Building/go-to-rooms";
  });
}

function deletebuilding(buildingId) {
  fetch("/delete-building", {
      method: "POST",
      body: JSON.stringify({ buildingId: buildingId }),
  }).then((_res) => {
      window.location.href = "/Dashboard/Buildings";
  });
}