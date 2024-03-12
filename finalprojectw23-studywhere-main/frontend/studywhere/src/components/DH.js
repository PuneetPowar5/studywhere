import roomData from "../data/dh.json";
import { useState } from "react";
import { Popup, Button } from "semantic-ui-react";
import Navbar from "./Navbar";
import "./DH.css";

function DH() {
  const [searchTerm, setSearchTerm] = useState("");
  return (
    <div>
      <Navbar />
      <input
        type="text"
        className="input"
        placeholder="Group or Single?"
        onChange={(event) => {
          setSearchTerm(event.target.value);
        }}
      />
      <table class="ui celled table">
        <thead>
          <tr>
            <th>ROOM</th>
            <th>Image</th>
            <th>Availability</th>
            <th>Event</th>
            <th>Occupancy</th>
          </tr>
        </thead>
        <tbody>
          {roomData
            .filter((data) => {
              if (searchTerm == "") {
                return data;
              } else if (
                data.properties.Type.toLowerCase().includes(
                  searchTerm.toLowerCase()
                )
              ) {
                return data;
              } else if (
                Number(data.properties.Occupancy) -
                  Number(data.properties.Sitting) >=
                Number(searchTerm)
              ) {
                return data;
              }
            })
            .map((room) => {
              if (room.properties.ROOM == 2060) {
                return (
                  <>
                    <tr>
                      <td data-label="ROOM">{room.properties.ROOM}</td>
                      <td data-label="Image">
                        <Popup
                          content={
                            <img
                              src={require("../data/Images/DH/2060.png")}
                            ></img>
                          }
                          trigger={<Button>Show Image</Button>}
                        />
                      </td>
                      <td data-label="Availability">
                        {room.properties.Availability}
                      </td>
                      <td data-label="Event">{room.properties.Event}</td>
                      <td data-label="Occupancy">
                        {room.properties.Sitting +
                          "/" +
                          room.properties.Occupancy}
                      </td>
                    </tr>
                  </>
                );
              } else if (room.properties.ROOM == 2070) {
                return (
                  <>
                    <tr>
                      <td data-label="ROOM">{room.properties.ROOM}</td>
                      <td data-label="Image">
                        <Popup
                          content={
                            <img
                              src={require("../data/Images/DH/2070.png")}
                            ></img>
                          }
                          trigger={<Button>Show Image</Button>}
                        />
                      </td>
                      <td data-label="Availability">
                        {room.properties.Availability}
                      </td>
                      <td data-label="Event">{room.properties.Event}</td>
                      <td data-label="Occupancy">
                        {room.properties.Sitting +
                          "/" +
                          room.properties.Occupancy}
                      </td>
                    </tr>
                  </>
                );
              } else if (room.properties.ROOM == 2080) {
                return (
                  <>
                    <tr>
                      <td data-label="ROOM">{room.properties.ROOM}</td>
                      <td data-label="Image">
                        <Popup
                          content={
                            <img
                              src={require("../data/Images/DH/2080.png")}
                            ></img>
                          }
                          trigger={<Button>Show Image</Button>}
                        />
                      </td>
                      <td data-label="Availability">
                        {room.properties.Availability}
                      </td>
                      <td data-label="Event">{room.properties.Event}</td>
                      <td data-label="Occupancy">
                        {room.properties.Sitting +
                          "/" +
                          room.properties.Occupancy}
                      </td>
                    </tr>
                  </>
                );
              } else if (room.properties.ROOM == 3000) {
                return (
                  <>
                    <tr>
                      <td data-label="ROOM">{room.properties.ROOM}</td>
                      <td data-label="Image">
                        <Popup
                          content={
                            <img
                              src={require("../data/Images/DH/3000.png")}
                            ></img>
                          }
                          trigger={<Button>Show Image</Button>}
                        />
                      </td>
                      <td data-label="Availability">
                        {room.properties.Availability}
                      </td>
                      <td data-label="Event">{room.properties.Event}</td>
                      <td data-label="Occupancy">
                        {room.properties.Sitting +
                          "/" +
                          room.properties.Occupancy}
                      </td>
                    </tr>
                  </>
                );
              } else if (room.properties.ROOM == 4001) {
                return (
                  <>
                    <tr>
                      <td data-label="ROOM">{room.properties.ROOM}</td>
                      <td data-label="Image">
                        <Popup
                          content={
                            <img
                              src={require("../data/Images/DH/4001.png")}
                            ></img>
                          }
                          trigger={<Button>Show Image</Button>}
                        />
                      </td>
                      <td data-label="Availability">
                        {room.properties.Availability}
                      </td>
                      <td data-label="Event">{room.properties.Event}</td>
                      <td data-label="Occupancy">
                        {room.properties.Sitting +
                          "/" +
                          room.properties.Occupancy}
                      </td>
                    </tr>
                  </>
                );
              } else {
                return (
                  <>
                    <tr>
                      <td data-label="ROOM">{room.properties.ROOM}</td>
                      <td data-label="Image">{room.properties.Image}</td>
                      <td data-label="Availability">
                        {room.properties.Availability}
                      </td>
                      <td data-label="Event">{room.properties.Event}</td>
                      <td data-label="Occupancy">
                        {room.properties.Sitting +
                          "/" +
                          room.properties.Occupancy}
                      </td>
                    </tr>
                  </>
                );
              }
            })}
        </tbody>
      </table>
    </div>
  );
}

export default DH;

