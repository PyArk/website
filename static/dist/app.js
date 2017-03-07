'use strict';

function getMeetups(url) {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.send();

        xhr.addEventListener('load', () => resolve(xhr.responseText));
        xhr.addEventListener('error', () => reject(xhr.responseText));
        xhr.addEventListener('abort', () => reject(xhr.responseText));
    });
}

window.addEventListener('DOMContentLoaded', function () {
    const meetupsContainer = document.getElementById('meetups-list');
    if (meetupsContainer) {
        const url = meetupsContainer.dataset.meetupsUrl;
        console.log(url);
        getMeetups(url).then((result) => {
            console.log(result);
            meetupsContainer.innerHTML = result;
        });
    }
});
