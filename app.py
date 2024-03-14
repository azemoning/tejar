import streamlit as st
import subprocess

destination_address = st.text_input("Destination address (Hostname/IP Address)") # 127.0.0.1
destination_port = st.text_input("Destination port") # 34831
destination_protocol = st.selectbox(
    "Select destination protocol",
    ("TCP", "UDP"),
    index=None,
    placeholder="TCP/UDP?"
)

is_submitted = st.button("Test Connection")

animation_placeholder = st.empty()

if is_submitted:
    with animation_placeholder.container():

        if destination_protocol == "TCP":
            nc_command = ["nc", "-vz", "-t", destination_address, destination_port]
            
            try:
                result = subprocess.check_output(nc_command, encoding='utf-8', stderr=subprocess.STDOUT)
                if "succeeded" in result:
                    st.success(f"Connected to {destination_address} {destination_protocol}/{destination_port}", icon="✅")
            except subprocess.CalledProcessError as err:
                if "refused" in err.output:
                    st.error(f"Connection failed to {destination_address} {destination_protocol}/{destination_port}", icon="❌")
                else:
                    st.error(err.output)

        if destination_protocol == "UDP":
            nc_command = ["nc", "-vz", "-u", destination_address, destination_port]
            
            try:
                result = subprocess.check_output(nc_command, encoding='utf-8', stderr=subprocess.STDOUT)
                if "succeeded" in result:
                    st.success(f"Connected to {destination_address} {destination_protocol}/{destination_port}", icon="✅")
            except subprocess.CalledProcessError as err:
                if "refused" in err.output:
                    st.error(f"Connection failed to {destination_address} {destination_protocol}/{destination_port}", icon="❌")
                else:
                    st.error(err.output)