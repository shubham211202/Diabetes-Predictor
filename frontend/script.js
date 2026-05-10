async function predict() {

    const resultBox = document.getElementById("result");

    resultBox.innerText = "Analyzing health data...";

    const data = {

        Age: Number(document.getElementById("Age").value),

        Gender: document.getElementById("Gender").value,

        BMI: Number(document.getElementById("BMI").value),

        Glucose: Number(document.getElementById("Glucose").value),

        BloodPressure:
            Number(document.getElementById("BloodPressure").value),

        HbA1c:
            Number(document.getElementById("HbA1c").value),

        Cholesterol:
            Number(document.getElementById("Cholesterol").value),

        FamilyHistory:
            Number(document.getElementById("FamilyHistory").value),

        PhysicalActivity:
            document.getElementById("PhysicalActivity").value,

        Smoking:
            Number(document.getElementById("Smoking").value),

        // Hidden default value
        Insulin: 120
    };

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)
            }
        );

        const result = await response.json();

        if(result.prediction === "Diabetic"){

            resultBox.innerHTML =
                "⚠️ High Risk of Diabetes";

            resultBox.style.background = "#fee2e2";
            resultBox.style.color = "#991b1b";

        }else{

            resultBox.innerHTML =
                "✅ Low Risk of Diabetes";

            resultBox.style.background = "#dcfce7";
            resultBox.style.color = "#166534";
        }

    } catch (error) {

        resultBox.innerText =
            "Error connecting to backend";
    }
}