'use strict';

function getMeetups(url) {
    return new Promise(function (resolve, reject) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.send();

        xhr.addEventListener('load', function () {
            return resolve(xhr.responseText);
        });
        xhr.addEventListener('error', function () {
            return reject(xhr.responseText);
        });
        xhr.addEventListener('abort', function () {
            return reject(xhr.responseText);
        });
    });
}

window.addEventListener('DOMContentLoaded', function () {
    var meetupsContainer = document.getElementById('meetups-list');
    if (meetupsContainer) {
        getMeetups(meetupsContainer.dataset.meetupsUrl).then(function (result) {
            return meetupsContainer.innerHTML = result;
        });
    }
});

