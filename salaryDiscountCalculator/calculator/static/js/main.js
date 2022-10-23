let form = document.getElementById("salaryForm");
form.addEventListener("submit", makePostAndRender);

function makePostAndRender(event) {
    event.preventDefault();
    let baseSalary = document.getElementById("base_salary").value;
    let bonifications = document.getElementById('bonifications').value;
    let extraHours = document.getElementById('extra_hours').value;
    let data = {
        'baseSalary': baseSalary,
        'bonifications': (bonifications) ? bonifications : 0,
        'extraHours': (extraHours) ? extraHours : 0
    };
    let url = "http://localhost:8000/calculator/menu-principal/";
    let xhr = new XMLHttpRequest();
    const modal = new bootstrap.Modal(document.getElementById('staticModal'));

    //MODAL
    xhr.onload = () => {
        //Display the modal
        console.log(xhr.responseText);
        let result = JSON.parse(xhr.responseText);
        
        document.getElementById("baseSalaryP").innerHTML = result["baseSalary"] + "$ DOP";
        document.getElementById("bonificationsP").innerHTML = result["bonifications"] + "$ DOP";
        document.getElementById("extraHours").innerHTML = result["extraHours"] + "$ DOP";
        document.getElementById("sfs").innerHTML = result["sfs"] + "$ DOP";
        document.getElementById("afp").innerHTML = result["afp"] + "$ DOP";
        document.getElementById("isr").innerHTML = result["isr"] + "$ DOP";
        document.getElementById("retentions").innerHTML = result["retentions"] + "$ DOP";
        document.getElementById("netSalary").innerHTML = result["netSalary"] + "$ DOP";
        
        modal.toggle(); 
    }
        
    xhr.open("POST", url, true);
    //Making a POST REQUEST        

    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.setRequestHeader("Accept", "application/json");
    
    xhr.send(JSON.stringify(data));
}