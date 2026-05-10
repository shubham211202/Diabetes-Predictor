async function predict() {

    const resultBox = document.getElementById("result");

    resultBox.innerHTML = "🔍 Analyzing health data...";

    // Get form data
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

    // Basic validation
    if (
        !data.Age ||
        !data.BMI ||
        !data.Glucose ||
        !data.BloodPressure ||
        !data.HbA1c ||
        !data.Cholesterol
    ) {

        resultBox.innerHTML =
            "⚠️ Please fill all required fields.";

        resultBox.style.background = "#fef3c7";
        resultBox.style.color = "#92400e";

        return;
    }

    try {

        // API request
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

        // Diabetic result
        if (result.prediction === "Diabetic") {

            resultBox.innerHTML =
                "⚠️ High Risk of Diabetes";

            resultBox.style.background = "#fee2e2";
            resultBox.style.color = "#991b1b";

        }

        // Non-diabetic result
        else {

            resultBox.innerHTML =
                "✅ Low Risk of Diabetes";

            resultBox.style.background = "#dcfce7";
            resultBox.style.color = "#166534";
        }

    }

    catch (error) {

        resultBox.innerHTML =
            "❌ Error connecting to backend";

        resultBox.style.background = "#fee2e2";
        resultBox.style.color = "#991b1b";
    }
}