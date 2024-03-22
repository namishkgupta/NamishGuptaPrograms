function calculatPosition() {
    const origin = document.getElementById('origin').value;
    const state = document.getElementById('state').value; 
    
    const mapUrl = "https://maps.google.com/maps?q="+ origin + "%2C%20" + state + "&t=&z=13&ie=UTF8&iwloc=&output=embed";

    const mapIframe = document.getElementById('map-iframe');

    mapIframe.setAttribute('src', mapUrl);
}
