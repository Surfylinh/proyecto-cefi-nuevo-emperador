document.addEventListener("DOMContentLoaded", function () {

    const ball = document.querySelector(".simulation-ball");

    const timeDisplay = document.querySelector("#simulation-time");
    const heightDisplay = document.querySelector("#simulation-height");
    const velocityDisplay = document.querySelector("#simulation-velocity");


    // If there is no simulation, stop here.
    if (!ball || !timeDisplay || !heightDisplay || !velocityDisplay) {
        return;
    }


    // Values received from Flask
    const simulation =
    document.querySelector(".simulation-container");

const h0 =
    Number(simulation.dataset.h0);

const v0 =
    Number(simulation.dataset.v0);

const g =
    Number(simulation.dataset.g);

const tMax =
    Number(simulation.dataset.tmax);


    if (h0 <= 0 || tMax <= 0) {
        return;
    }


    // --------------------------------
    // ANIMATION SETTINGS
    // --------------------------------

    const scene = document.querySelector(".simulation-scene");

    const startPosition = 35;

    const groundPosition =
        scene.clientHeight - 45 - 28;


    let startTime = null;


    // --------------------------------
    // SIMULATION
    // --------------------------------

    function animate(timestamp) {

        if (!startTime) {
            startTime = timestamp;
        }


        // Convert milliseconds to seconds
        let elapsed =
            (timestamp - startTime) / 1000;


        // Don't go beyond the selected time
        if (elapsed > tMax) {
            elapsed = tMax;
        }


        // --------------------------------
        // PHYSICS EQUATIONS
        // --------------------------------

        let height =
            h0 + v0 * elapsed - 0.5 * g * elapsed ** 2;


        let velocity =
            v0 - g * elapsed;


        // Don't let the object go below the ground
        if (height < 0) {
            height = 0;
        }


        // --------------------------------
        // CONVERT METERS → PIXELS
        // --------------------------------

        const percentage =
            (h0 - height) / h0;


        const ballPosition =
            startPosition +
            percentage *
            (groundPosition - startPosition);


        // --------------------------------
        // MOVE BALL
        // --------------------------------

        ball.style.top =
            ballPosition + "px";


        // --------------------------------
        // UPDATE INFORMATION
        // --------------------------------

        timeDisplay.textContent =
            elapsed.toFixed(2) + " s";


        heightDisplay.textContent =
            height.toFixed(2) + " m";


        velocityDisplay.textContent =
            velocity.toFixed(2) + " m/s";


        // --------------------------------
        // CONTINUE
        // --------------------------------

        if (elapsed < tMax && height > 0) {

            requestAnimationFrame(animate);

        } else {

            // Make sure the final position is exact
            ball.style.top =
                groundPosition + "px";

        }

    }


    requestAnimationFrame(animate);

});