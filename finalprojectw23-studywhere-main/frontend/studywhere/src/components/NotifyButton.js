import React from "react";
import Button from "@mui/material/Button";
import { AiFillBell } from "react-icons/ai";
import "./NotifyButton.css";

class NotifyButton extends React.Component {
  state = {
    liked: false,
    isError: false,
  };

  onClick = () => {
    this.setState({ liked: !this.state.liked, isError: !this.state.isError });
  };

  render() {
    return (
      <div className="like">
        <Button
          variant="contained"
          color={this.state.isError ? "secondary" : "primary"}
          onClick={this.onClick}
          startIcon={<AiFillBell />}
          size="large"
        >
          {this.state.liked ? "Notified" : "Notify"}
        </Button>
      </div>
    );
  }
}

export default NotifyButton;
