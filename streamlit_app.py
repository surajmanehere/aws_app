import streamlit as st
import folium
from folium import Marker
from geopy.geocoders import Nominatim

# Initialize the geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

# Streamlit app
def main():
    st.title("Location Search on Map")

    # Input for location search
    location_input = st.text_input("Enter a location:")

    if st.button("Search"):
        if location_input:
            # Geocode the location to get latitude and longitude
            location = geolocator.geocode(location_input)

            if location:
                lat, lon = location.latitude, location.longitude
                st.success(f"Location found: {location.address}")

                # Create a map centered around the searched location
                m = folium.Map(location=[lat, lon], zoom_start=15)

                # Add a marker for the location
                Marker([lat, lon], tooltip=location.address).add_to(m)

                # Display the map
                st_map = m._repr_html_()
                st.components.v1.html(st_map, height=500)

            else:
                st.error("Location not found. Please try a different search.")
        else:
            st.warning("Please enter a location to search.")

if __name__ == "__main__":
    main()
