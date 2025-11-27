import os
import smtplib
import ssl
from email.message import EmailMessage

import streamlit as st


SMTP_HOST = os.getenv("PORTFOLIO_SMTP_HOST")
SMTP_PORT = os.getenv("PORTFOLIO_SMTP_PORT", "587")
SMTP_USERNAME = os.getenv("PORTFOLIO_SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("PORTFOLIO_SMTP_PASSWORD")
SMTP_SENDER = os.getenv("PORTFOLIO_SMTP_SENDER", SMTP_USERNAME)
CONTACT_RECIPIENT = os.getenv("PORTFOLIO_CONTACT_RECIPIENT", SMTP_USERNAME)


def _email_settings_ready() -> bool:
    required = [SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, CONTACT_RECIPIENT]
    return all(required)


def _send_contact_email(name: str, email: str, subject: str, message: str) -> tuple[bool, str]:
    """Send the contact form contents via SMTP."""

    if not _email_settings_ready():
        return False, "Email delivery is not configured."

    try:
        port = int(SMTP_PORT)
    except (TypeError, ValueError):
        port = 587

    email_message = EmailMessage()
    email_message["Subject"] = f"Portfolio contact: {subject.strip() or 'No subject'}"
    if SMTP_SENDER:
        email_message["From"] = SMTP_SENDER
    if CONTACT_RECIPIENT:
        email_message["To"] = CONTACT_RECIPIENT

    body_lines = [
        "New message submitted via portfolio contact form:",
        "",
        f"Name: {name}",
        f"Email: {email}",
        f"Subject: {subject}",
        "",
        "Message:",
        message,
    ]
    email_message.set_content("\n".join(body_lines))

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(SMTP_HOST, port, timeout=30) as server:
            server.starttls(context=context)
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(email_message)
        return True, "Message sent successfully!"
    except Exception as exc:  # noqa: BLE001
        return False, f"Unable to send message: {exc}"


def show():
    """Contact page of the portfolio"""
    
    st.markdown("<h1 class='section-title'>📬 Get In Touch</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
        <div style='text-align: center; margin: 2rem 0;'>
            <p style='font-size: 1.1rem; color: #b0b0b0;'>
                I'd love to hear from you! Feel free to reach out through any of the following channels.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Contact Information
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='contact-info'>
                <h3 style='text-align: center;'>📧 Email</h3>
                <p style='text-align: center;'>
                    <a href='mailto:uttaranganguly20@gmail.com'>
                        uttaranganguly20@gmail.com
                    </a>
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='contact-info'>
                <h3 style='text-align: center;'>🐙 GitHub</h3>
                <p style='text-align: center;'>
                    <a href='https://github.com/uttaranganguly567' target='_blank'>
                        @uttaranganguly567
                    </a>
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class='contact-info'>
                <h3 style='text-align: center;'>💼 LinkedIn</h3>
                <p style='text-align: center;'>
                    <a href='https://www.linkedin.com/in/uttaran-ganguly/' target='_blank'>
                        Uttaran Ganguly
                    </a>
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 💬 Direct Message")

    settings_ready = _email_settings_ready()
    if not settings_ready:
        st.info(
            "Direct message delivery is currently inactive. Set the SMTP environment variables "
            "documented in the README to start receiving emails."
        )
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            if name and email and subject and message:
                success, feedback = _send_contact_email(name, email, subject, message)
                if success:
                    st.success(
                        f"Thanks {name}! Your message was sent.\n\n"
                        "I'll reach out to you shortly."
                    )
                    st.toast("Message sent successfully ✅", icon="✅")
                else:
                    st.error(feedback)
            else:
                st.error("Please fill in all fields!")
    
    st.markdown("---")
    
    st.markdown("""
        <div style='text-align: center; color: #707070; margin-top: 2rem;'>
            <p>I'll get back to you as soon as I can!</p>
        </div>
    """, unsafe_allow_html=True)
