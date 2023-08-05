import React from "react";
import "./footer.css";
import linkedinIcon from "../../images/linkedin.svg";
import instagramIcon from "../../images/instagram.svg";
import facebookIcon from "../../images/facebook.svg";

const Footer = () => (
  <footer className="page-footer font-small blue pt-4">
    <div className=" footer-center">
      <ul className="list-unstyled d-flex justify-content-between">
        <li>
          <a href="https://www.linkedin.com/company/alfaengenhariaemontagens/?viewAsMember=true" target="_blank" rel="noopener noreferrer">
            <img className="icon" src={linkedinIcon} alt="LinkedIn" />
          </a>
        </li>
        <li>
          <a href="https://www.instagram.com/alfaengenharia.ind/" target="_blank" rel="noopener noreferrer">
            <img className="icon" src={instagramIcon} alt="Instagram" />
          </a>
        </li>
        <li>
          <a href="https://www.facebook.com/alfaengenharia.ind" target="_blank" rel="noopener noreferrer">
            <img className="icon" src={facebookIcon} alt="Facebook" />
          </a>
        </li>
      </ul>
    </div>
  </footer>
);

export default Footer;
