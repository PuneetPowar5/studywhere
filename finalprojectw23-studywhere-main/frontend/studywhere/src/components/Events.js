import eventData from "../data/events.json";
import Navbar from "./Navbar";

function Events() {
  return (
    <div>
      <Navbar />
      <table class="ui celled table">
        <thead>
          <tr>
            <th>Event</th>
            <th>Location</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {eventData.map((event) => {
            return (
              <tr>
                <td data-label="Event">{event.properties.Event}</td>
                <td data-label="Location">{event.properties.Location}</td>
                <td data-label="Date">{event.properties.Date}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export default Events;
