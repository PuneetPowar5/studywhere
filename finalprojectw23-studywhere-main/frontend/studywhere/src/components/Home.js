import Map, { Marker, Popup } from "react-map-gl";
import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import buildingData from "./../data/buliding-data.json";
import "mapbox-gl/dist/mapbox-gl.css";
import mappin from "./../map-pin.svg";
import "./Home.css";
import { Link } from "react-router-dom";
import Navbar from "./Navbar";

function Home() {
  const [selectedBuilding, setSelectedBuilding] = useState(null);

  return (
    <div>
      <Navbar />
      <Map
        initialViewState={{
          latitude: 43.547867,
          longitude: -79.660942,
          zoom: 16,
        }}
        style={{ width: "100vw", height: "100vh" }}
        mapStyle="mapbox://styles/mapbox/streets-v12"
        mapboxAccessToken="pk.eyJ1IjoicHVuZWV0cG93YXIxMCIsImEiOiJjbGRqeGVycTUwMTZrM3dsYzcza2hraDNjIn0.KX4tmSLew05lOrz0MAONrg"
      >
        {buildingData.features.map((data) => (
          <Marker
            key={data.properties.PARK_ID}
            latitude={data.geometry.coordinates[0]}
            longitude={data.geometry.coordinates[1]}
          >
            <button
              className="marker"
              onClick={(e) => {
                e.preventDefault();
                setSelectedBuilding(data);
              }}
            >
              <img src={mappin} alt="MARKER" />
            </button>
          </Marker>
        ))}
        {selectedBuilding ? (
          <Popup
            longitude={selectedBuilding.geometry.coordinates[1]}
            latitude={selectedBuilding.geometry.coordinates[0]}
            closeOnClick={false}
            onClose={() => {
              setSelectedBuilding(null);
            }}
          >
            <div>
              <h2>{selectedBuilding.properties.NAME}</h2>
              <h3>{selectedBuilding.properties.EVENTS}</h3>
              <p>{selectedBuilding.properties.ROOMS}</p>
            </div>

            <Link to={"/" + selectedBuilding.properties.NAME}>
              <Button
                variant="outlined"
                color="primary"
                style={{ fontSize: "1.5em" }}
              >
                More Info
              </Button>
            </Link>
          </Popup>
        ) : null}
      </Map>
    </div>
  );
}

export default Home;

