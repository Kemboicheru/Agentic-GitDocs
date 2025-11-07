import from byllm.llm { Model }
import from email.mime.text { MIMEText }
import smtplib;
import os;

import from utils { get_current_datetime }

glob llm = Model(model_name="gpt-4o", verbose=False);
