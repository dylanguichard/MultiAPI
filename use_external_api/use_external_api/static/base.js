function goto(url) {
	window.location.href = window.location.origin + "/" + url;
}

function like(elId, type, csrf_token) {
	let data = {
		elId: elId,
		type: type,
	};
	let formData = new FormData();
	formData.append("elId", elId);
	formData.append("type", type);
	fetch("http://127.0.0.1:8000/like/", {
		headers: {
			"X-CSRFToken": csrf_token,
			"Content-Type": "application/json",
		},
		credentials: "same-origin",
		method: "post",
		body: JSON.stringify(data),
	});
}

function unlike(elId, type, csrf_token) {
	let data = {
		elId: elId,
		type: type,
	};
	let formData = new FormData();
	formData.append("elId", elId);
	formData.append("type", type);
	fetch("http://127.0.0.1:8000/unlike/", {
		headers: {
			"X-CSRFToken": csrf_token,
			"Content-Type": "application/json",
		},
		credentials: "same-origin",
		method: "post",
		body: JSON.stringify(data),
	});
}
