let form = document.getElementById("salaryForm");

form.addEventListener("submit", async (event) => {
    if (event.submitter.matches("#submitButton")){
        event.preventDefault();
        
        let baseSalary = document.getElementById("base_salary").value;
        let url = "http://localhost:8000/calculator/menu-principal/";
        let data = {'baseSalary':baseSalary};
        let xhr = new XMLHttpRequest();
        
        //Making a POST REQUEST
        xhr.onload = () => console.log(xhr.responseText);
        
        xhr.open("POST", url, true);

        xhr.setRequestHeader("Accept", "application/json");
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

        xhr.send(JSON.stringify(data));
    }
});