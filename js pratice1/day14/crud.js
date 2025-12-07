
let data = [];
let editIndex = -1;

function createData() {
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let phone = document.getElementById('phone').value;
    let college = document.getElementById('college').value;

    // validation
    if (name === "" || email === "" || phone === "" || college === "") {
        alert("Please fill all fields!");
        return;
    }

    // create or update
    if (editIndex === -1) {
        data.push({ name, email, phone, college });
    } else {
        data[editIndex].name = name;
        data[editIndex].email = email;
        data[editIndex].phone = phone;
        data[editIndex].college = college;
        editIndex = -1;
    }

    // clear input fields
    document.getElementById('name').value = "";
    document.getElementById('email').value = "";
    document.getElementById('phone').value = "";
    document.getElementById('college').value = "";

    displayData();
}

// show table data
function displayData() {
    let tbody = document.getElementById("tbody");
    tbody.innerHTML = "";

    data.forEach((item, index) => {
        tbody.innerHTML += `
            <tr>
                <td>${item.name}</td>
                <td>${item.email}</td>
                <td>${item.phone}</td>
                <td>${item.college}</td>
                <td>
                    <button class="edit-btn" onclick="editData(${index})">Edit</button>
                    <button class="delete-btn" onclick="deleteData(${index})">Delete</button>
                </td>
            </tr>
        `;
    });
}

// edit function
function editData(index) {
    document.getElementById('name').value = data[index].name;
    document.getElementById('email').value = data[index].email;
    document.getElementById('phone').value = data[index].phone;
    document.getElementById('college').value = data[index].college;

    editIndex = index;
}

// delete function
function deleteData(index) {
    data.splice(index, 1);
    displayData();
}
