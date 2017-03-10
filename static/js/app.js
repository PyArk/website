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
        getMeetups(meetupsContainer.dataset.meetupsUrl)
            .then((result) => meetupsContainer.innerHTML = result);
    }
});
