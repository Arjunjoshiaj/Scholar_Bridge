fetch("http://localhost:8000/scholarships/")
    .then(response => response.json())
    .then(data => {
        let container = document.getElementById("scholarships");
        data.forEach(scholarship => {
            let div = document.createElement("div");
            div.innerHTML = `<h2>${scholarship.title}</h2> <a href="${scholarship.link}" target="_blank">Apply</a>`;
            container.appendChild(div);
        });
    })
    .catch(error => console.error("Error fetching scholarships:", error));
