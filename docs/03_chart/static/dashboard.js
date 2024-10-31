/* Fetch JSON and add chart to #display element. */
async function display() {
    const response = await fetch('http://127.0.0.1:5000/data');
    const data = await response.json();
    const display = document.querySelector('#chart');
    new chartXkcd.XY(display, data);
}
