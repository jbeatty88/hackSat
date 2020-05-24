from skyfield.api import load
from skyfield.sgp4lib import EarthSatellite
from skyfield.toposlib import Topos

if __name__ == '__main__':
    ts = load.timescale()
    t = ts.now()
    planets = load('de421.bsp')
    earth = planets['earth']
    tleLabel = "REDACT"
    tle1 = '1 13337U 98067A   20087.38052801 -.00000452  00000-0  00000+0 0  9995'
    tle2 = '2 13337  51.6460  33.2488 0005270  61.9928  83.3154 15.48919755219337'

    sat = EarthSatellite(tle1, tle2, tleLabel, ts)
    geocentric = sat.at(t)
    print("Geocentric Position:")
    print(geocentric.position.m, end=' METERS\n')
    print(geocentric.position.km, end=' KILOMETERS\n\n')

    subpoint = geocentric.subpoint()
    print("Point Directly below Sat:")
    print('Latitude:', subpoint.latitude)
    print('Longitude:', subpoint.longitude)
    print('Elevation (m):', int(subpoint.elevation.m), end='\n\n')

    washington_monument_topos = Topos('38.8895 N', '77.0353 W')
    difference = sat - washington_monument_topos
    print("Difference between Washington Monument and Sat:")
    print(difference, end='\n\n')

    topocentric = difference.at(t)
    print('Position of Sat relative to you:')
    print(topocentric.position.m, end=' METERS\n')
    print(topocentric.position.km, end=' KILOMETERS\n\n')

    altitude, azimuth, distance = topocentric.altaz()
    if altitude.degrees > 0:
        print('The Sat is above the horizon')
    print("Altitude: ", end=' ')
    print(altitude)
    print("Azimuth: ", end=' ')
    print(azimuth)
    print("Distance: ", end=' ')
    print(distance, end='\n\n')

    right_ascension, declination, dist = topocentric.radec()
    print("Position of Sat among the stars:")
    print("Right Ascension: ", end=' ')
    print(right_ascension)
    print("Declination: ", end=' ')
    print(declination)
    print("Distance: ", end=' ')
    print(dist)



