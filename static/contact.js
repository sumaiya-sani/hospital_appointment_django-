



$('#us3').locationpicker({
    location: {
      latitude: -8.681013,
      longitude: 115.23506410000005
    },
    radius: 0,
    inputBinding: {
      latitudeInput: $('#us3-lat'),
      longitudeInput: $('#us3-lon'),
      radiusInput: $('#us3-radius'),
      locationNameInput: $('#us3-address')
    },
    enableAutocomplete: true,
    onchanged: function (currentLocation, radius, isMarkerDropped) {
      // Uncomment line below to show alert on each Location Changed event
      //alert("Location changed. New location (" + currentLocation.latitude + ", " + currentLocation.longitude + ")");
    }
  });