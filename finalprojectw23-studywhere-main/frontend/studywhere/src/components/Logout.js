import React from "react";
import Button from "@mui/material/Button";
import "./Logout.css";

class Logout extends React.Component {
  refreshPage = () => {
    window.location.reload(false);
  };

  render() {
    return (
      <div className="logout">
        <Button
          variant="contained"
          color={"primary"}
          onClick={this.refreshPage}
          size="large"
        >
          Logout
        </Button>
      </div>
    );
  }
}

export default Logout;
