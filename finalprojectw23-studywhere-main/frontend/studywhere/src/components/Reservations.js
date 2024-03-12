import NotifyButton from "./NotifyButton";
import reservationData from "../data/reservations.json";
import Navbar from "./Navbar";

function Reservations() {
  return (
    <div>
      <Navbar />
      <table class="ui celled table">
        <thead>
          <tr>
            <th>Reservation</th>
            <th>Date</th>
            <th>Notifications</th>
          </tr>
        </thead>
        <tbody>
          {reservationData.map((reservation) => {
            return (
              <tr>
                <td data-label="Reservation">
                  {reservation.properties.Reservation}
                </td>
                <td data-label="Date">{reservation.properties.Date}</td>
                <td data-label="Notifications">{<NotifyButton />}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export default Reservations;
