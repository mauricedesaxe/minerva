### COPYRIGHT

Subject to the existing rights of third parties, Space Exploration Technologies Corp. (SpaceX) is the owner of the copyright
in this work, and no portion hereof is to be copied, reproduced, or disseminated without the prior written consent of
SpaceX.


## © Space Exploration Technologies Corp. All rights reserved. ii



- 1.1 User’s Guide Purpose
- 1.2 Company Description
- 1.3 Falcon Program Overview
   - Falcon Launch Vehicle Safety
- 1.5 Falcon Reliability
      - 1.5.1 Engines
      - 1.5.2 Avionics
      - 1.5.3 Staging Architecture and Design
- 1.6 Pricing
   - Falcon Vehicle Overview
      - Falcon Heavy Vehicle Overview
         - Structure and Propulsion
         - Retention, Release and Separation Systems
         - Avionics, and Guidance, Navigation and Control
         - Coordinate Frame
   - Available Injection Orbits
         - Mass-to-Orbit Capability
         - Mass Properties
         - Launch Windows
         - Flight Attitude
         - Separation Attitude and Accuracy
      - Multiple Payloads
         - Secondary Payloads
   - Transportation Environments
         - Temperature, Humidity and Cleanliness
         - Flight Environments
      - 4.3.1 Loads
      - 4.3.2 Sine Vibration
      - 4.3.3 Acoustic
   - 4.3.4 Shock © Space Exploration Technologies Corp. All rights reserved. iii
   - 4.3.5 Random Vibration
   - 4.3.6 Electromagnetic
   - 4.3.7 Fairing Internal Pressure
   - 4.3.8 Payload Temperature Exposure during Flight
   - 4.3.9 Free Molecular Heating
      - Environmental Compatibility Verification
- Mechanical Interfaces
   - 5.1.1 Payload Adapters and Separation Systems
   - 5.1.2 Payload Fairings
      - Electrical Interfaces
   - 5.2.1 Connectivity during Payload Processing and on Launch Pad
   - 5.2.2 Falcon-to-Payload Command Interface
   - 5.2.3 Timing Services
      - Interface Compatibility Verification Requirements
- SpaceX East Coast Launch Facilities
   - 6.1.1 Cape Canaveral Space Force Station, Florida
   - 6.1.2 Kennedy Space Center, Florida
   - 6.1.3 CCSFS & KSC Personnel Accommodations
      - Vandenberg Space Force Base, California
   - 6.2.1 VSFB Personnel Accommodations
      - Headquarters—Hawthorne, CA
      - Rocket Development Facility—McGregor, TX
      - Government Outreach and Legal Affairs—Washington, DC
- Contracting
   - Mission Management
   - Standard Services
   - Schedule
   - Customer Deliverables
   - Overview and Schedule
      - Spacecraft Delivery and Transportation
      - Spacecraft Processing © Space Exploration Technologies Corp. All rights reserved. iv
      - Joint Operations and Integration
      - Launch Operations
   - 8.5.1 Organization
   - 8.5.2 Spacecraft Control Center
   - 8.5.3 Launch Control
   - 8.5.4 Rollout, Erection and Pad Operations
   - 8.5.5 Countdown
   - 8.5.6 Recycle and Scrub
      - Flight Operations
   - 8.6.1 Liftoff and Ascent
   - 8.6.2 Spacecraft Separation
   - 8.6.3 Contamination and Collision Avoidance
   - 8.6.4 Post Launch Reports
   - 8.6.5 Disposal
      - Sample Mission Profile
- Safety Requirements
      - Hazardous Systems and Operations
      - Waivers
      - List of Figures
         - List of Tables
         - List of Acronyms
         - Change Log


The Falcon launch vehicle user’s guide is a planning document provided for customers of SpaceX (Space Exploration
Technologies Corp.). This document is applicable to the Falcon vehicle configurations with a 5.2 m ( 17 - ft) diameter
fairing and the related launch service (Section 2 ).

This user’s guide is intended for pre-contract mission planning and for understanding SpaceX’s standard services. The
user’s guide is not intended for detailed design use. Data for detailed design purposes will be exchanged directly between
a SpaceX customer and a SpaceX mission manager.

SpaceX reserves the right to update this user’s guide as required. Future revisions are assumed to always be in process
as SpaceX gathers additional data and works to improve its launch vehicle design.

SpaceX offers a family of launch vehicles that improves launch reliability and increases access to space. The company
was founded on the philosophy that simplicity, reliability and cost effectiveness are closely connected. We approach all
elements of launch services with a focus on simplicity to both increase reliability and lower cost. The SpaceX corporate
structure is flat and business processes are lean, resulting in fast decision-making and product delivery. SpaceX
products are designed to require low-infrastructure facilities with little overhead, while vehicle design teams are co-
located with production and quality assurance staff to tighten the critical feedback loop. The result is highly reliable and
producible launch vehicles with quality embedded throughout the process.

Established in 2002 by Elon Musk, the founder of Tesla Motors, PayPal and the Zip2 Corporation, SpaceX has developed
and flown the Falcon 1 light-lift launch vehicle, the Falcon 9 medium-lift launch vehicle, the Falcon Heavy heavy-lift launch
vehicle, the most powerful operational rocket in the world by a factor of two, and Dragon, which is the first commercially
produced spacecraft to visit the International Space Station.

SpaceX has built a launch manifest that includes a broad array of commercial, government and international customers.
In 2008 , NASA selected the SpaceX Falcon 9 launch vehicle and Dragon spacecraft for the International Space Station
Cargo Resupply Services contract. NASA has also awarded SpaceX contracts to develop the capability to transport
astronauts to space as well as to launch scientific satellites. SpaceX’s first crewed test flight with the Crew Dragon
spacecraft launched in May 2020, carrying NASA astronauts Douglas Hurley and Robert Behnken to the International
Space Station and safely returning them to Earth two months later. NASA has certified the Falcon 9 / Crew Dragon
system for human spaceflight, and SpaceX is providing operational missions to the International Space Station under
the Commercial Crew Program, as well providing the capability to launch commercial astronauts to space. In addition,
SpaceX services the National Security community and is on contract with the U.S. Space Force for multiple missions on
the Falcon family of launch vehicles.

SpaceX has state-of-the-art production, testing, launch and operations facilities. SpaceX design and manufacturing
facilities are conveniently located near the Los Angeles International Airport. This location allows the company to
leverage Southern California’s rich aerospace talent pool. The company also operates cutting-edge propulsion and
structural test facilities in Central Texas, along with launch sites in Florida and California, and a commercial orbital launch
site in development in South Texas.


Drawing on a history of prior launch vehicle and engine programs, SpaceX privately developed the Falcon family of launch
vehicles. Component developments include first- and second-stage engines, cryogenic tank structures, avionics,
guidance and control software, and ground support equipment.

With the Falcon 9 and Falcon Heavy launch vehicles, SpaceX is able to offer a full spectrum of medium- and heavy-lift
launch capabilities to its customers (Figure 1 - 1 ), as well as small and micro satellite launch capabilities via its Rideshare
Program. SpaceX currently operates Falcon launch facilities at Cape Canaveral Space Force Station (CCSFS), Kennedy
Space Center (KSC), and Vandenberg Space Force Base (VSFB) and can deliver payloads to a wide range of inclinations
and altitudes, from low Earth orbit (LEO) to geosynchronous transfer orbit (GTO) to escape trajectories for interplanetary
missions.

The Falcon family has conducted successful flights to the International Space Station (ISS), LEO, highly elliptical orbit
(HEO), GTO, and Earth-escape trajectories. As of the end of 2020 , SpaceX has completed over 100 Falcon launches,
making it the most flown U.S. launch vehicle currently in operation.

Reusability is an integral part of the Falcon program. SpaceX pioneered reusability with the first re-flight of an orbital
class rocket in 2017. As of August 2021, SpaceX has re-flown rockets more than 65 times, with a 100% success rate.
Since 2018, SpaceX had more missions launching with a flight-proven rocket than a first flight rocket. SpaceX also
started re-flying fairings in late 2019, and as of the end of 2020 has re-flown more than 40 fairing halves with a 100%
success rate. By re-flying boosters and fairings, SpaceX increases reliability and improves its designs and procedures
by servicing and inspecting hardware as well as incorporating lessons that can only be learned from flight.

The Falcon launch vehicles were designed from the beginning to meet NASA human-rated safety margins. We continue
to push the limits of rocket technology as we design the safest crew transportation system ever flown while
simultaneously advancing toward fully reusable launch vehicles. Our emphasis on safety has led to advancements such
as increased structural factors of safety, greater redundancy and rigorous fault mitigation. Because SpaceX produces
one Falcon core vehicle, satellite customers benefit from the high design standards required to safely transport crew.
The major safety features are listed in more detail in Table 1 - 1.


```
Design/Operations Feature Safety Benefit
Designed to NASA human-rating margins and safety
requirements
```
```
Improves reliability for payloads without crew through
increased factors of safety, redundancy and fault
mitigation
Horizontal manufacturing, processing and integration Reduces work at height during numerous
manufacturing, processing and integration procedures,
and eliminates many overhead operations
All-liquid propulsion architecture; fuel and oxidizer are
stored separately on the ground and in the vehicle.
Propellant is not loaded into the vehicle until the vehicle
is erected for launch
```
```
Significantly improves safety by eliminating hazardous
ground handling operations required for systems that
use solid propellant cores or boosters
```
```
Rocket-grade kerosene and liquid oxygen as primary
propellants
```
```
Reduces health hazards to processing, integration, and
recovery personnel compared to systems that use high
toxicity primary propellants
Non-explosive, pneumatic release and separation
systems for stage separation and standard payload
fairing separation
```
```
Zero-debris separation systems significantly reduce
orbital debris signature, can be repeatedly tested during
the manufacturing process, and eliminate hazardous
pyrotechnic devices
Regular hardware-in-the-loop (HITL) software testing Complete verification of entire mission profile prior to
flight
```
A study^1 by The Aerospace Corporation found that 91% of known launch vehicle failures in the previous two decades
can be attributed to three causes: engine, avionics, and stage separation failures. With this in mind, SpaceX incorporated
key engine, avionics, and staging reliability features for high reliability at the architectural level of Falcon launch vehicles.
Significant contributors to reliability include:

As of the end of 2020 , the Merlin engine that powers the Falcon family of launch vehicles is the only new hydrocarbon
engine to be successfully developed and flown in the U.S. in the past 4 0 years. It has the highest thrust-weight ratio of
any boost engine ever made. The liquid-propelled Merlin powers the Falcon propulsion system. The engine features a
reliable turbopump design with a single shaft for the liquid oxygen pump, the fuel pump, and the turbine. The engine
uses a gas generator cycle instead of the more complex staged combustion cycle. The regeneratively cooled nozzle and
thrust chamber use a milled copper alloy liner that provides large heat flux margins. A pintle injector provides inherent
combustion stability.

Engine failure modes are minimized by eliminating separate subsystems where appropriate. For example, the first-stage
thrust vector control system pulls from the high-pressure rocket-grade kerosene system, rather than using a separate
hydraulic fluid and pressurization system. Using fuel as the hydraulic fluid eliminates potential failures associated with
a separate hydraulic system and with the depletion of hydraulic fluid.

The high-volume engine production required to fly 10 Merlin engines (Falcon 9) or 28 engines (Falcon Heavy) on every
launch results in high product quality and repeatability through process control and continuous production. Flying
several engines on each mission also quickly builds substantial engineering data and flight heritage.

(^1) Chang, I-Shih. “Space Launch Vehicle Reliability,” Aerospace Corporation Publication (2001).


During Falcon launch operations, the first stage is held on the ground after engine ignition while automated monitors
confirm nominal engine operation. An autonomous safe shutdown is performed if any off-nominal condition is detected.
Hold-on-pad operations, enabled by the launch vehicle’s all-liquid propulsion architecture and autonomous countdown
sequence, significantly reduce risks associated with engine start-up failures and underperformance.

By employing multiple first-stage engines, SpaceX offers the world’s first evolved expendable launch vehicle (EELV)-
class system with engine-out capability through much of first-stage flight. System-level vehicle management software
controls the shutdown of engines in response to off-nominal engine indications; this has been demonstrated in flight,
with 100% primary mission success. Although the likelihood of catastrophic engine failure is low, and failing engines are
designed to be shut down prior to a catastrophic failure, each engine is housed within its own metal bay to isolate it from
neighboring engines.

The second-stage Merlin Vacuum engine uses a fixed, non-deploying expansion nozzle, eliminating potential failure
modes in nozzle extension.

Falcon launch vehicle avionics, and guidance, navigation and control systems use a fault-tolerant architecture that
provides full vehicle single-fault tolerance and uses modern computing and networking technology to improve
performance and reliability. The fault tolerance is achieved either by isolating compartments within avionics boxes or by
using triplicated units of specific components. Both the first and second stages host their own multiple redundant
lithium-ion batteries to minimize the complexity of the electrical interface.

The two-stage Falcon 9 architecture was selected to minimize the number of stage separation events, eliminating
potential failure modes associated with third- and fourth-stage separations, as well as potential engine deployment and
ignition failure modes in the third and fourth stages. Falcon Heavy uses the same stage architecture as Falcon 9 with
the addition of two separating side cores.

The Falcon second-stage and Falcon Heavy side-boosters restraint, release, and separation systems use pneumatic
devices that provide low-shock release and positive force separation over a comparatively long stroke. The pneumatic
system allows for acceptance and functional testing of the actual flight hardware, which is not possible with a traditional
explosives-based separation system.

For each Falcon launch vehicle, SpaceX performs an exhaustive series of tests from the component to the vehicle
system level. The test program includes component-level flight acceptance and workmanship testing, structures load
and proof testing, flight system and propulsion subsystem-level testing, and full first- and second-stage testing up to full
system testing (including first- and second-stage static fire testing). In addition to testing environmental extremes (plus
margin), flight critical and workmanship sensitive hardware are tested to account for off-nominal conditions. For
example, stage separation tests are performed for off-nominal cases with respect to geometrical misalignment,
anomalous timing and sequencing.

The Falcon first stage is designed to survive atmospheric entry and to be recovered, handling both the rigors of the
ascent portion of the mission and the loads of the recovery portion. Stage recoverability also provides a unique
opportunity to examine recovered hardware and assess design and material selection in order to continually improve
Falcon 9 and Falcon Heavy.


The standard price for Falcon 9 and Falcon Heavy launch services can be found at
https://www.spacex.com/media/Capabilities&Services.pdf. Pricing includes range services, standard payload
integration and third-party liability insurance. Please see Section 7.3 for a complete description of standard services.
Nonstandard services are also available.


Descriptions and performance information in this user’s guide are for the Falcon 9 and Falcon Heavy fairing
configuration; please contact SpaceX for information about Dragon launch capabilities. Table 2 - 1 provides additional
details on Falcon 9 and Falcon Heavy dimensions and design characteristics.

Falcon 9 (Figure 2 - 1 ) is a two-stage launch vehicle powered by liquid
oxygen (LOX) and rocket-grade kerosene (RP-1). The vehicle is designed,
built and operated by SpaceX. Falcon 9 can be flown with a fairing or with
a SpaceX Dragon spacecraft. All first- and second-stage vehicle systems
are the same in the two configurations; only the payload interface to the
second stage changes between the fairing and Dragon configurations.

Falcon 9 was updated in the summer of 2015 to a Full Thrust
configuration from its previous v1.1 configuration (flown from 2013 –
summer 2015). Falcon 9 underwent further updates and first flew its Full
Thrust Block 5 configuration in spring 2018. The Falcon 9 Block 5
architecture focused on improving performance, reliability, and life of the
vehicle, as well as ensuring the vehicle’s ability to meet critical
government crewed and non-crewed mission requirements. Engine
performance on both stages was improved, releasing additional thrust
capability. Thermal protection shielding was modified to support rapid
recovery and refurbishment. Avionics designs, thrust structures, and
other components were upgraded for commonality, reliability, and
performance.

Falcon Heavy (Figure 2 - 2 ) is a two-stage, heavy-lift launch vehicle
powered by LOX and RP-1. It can transport more payload mass into LEO
or GTO than any other launch vehicle currently in operation.

Falcon Heavy is the most powerful launch vehicle in operation with more
than 5.1 million pounds of thrust at liftoff. Falcon Heavy builds on the
proven, highly reliable design of Falcon 9. Falcon Heavy’s first-stage
comprises three Falcon 9 first stages with enhancements provided to
strengthen the cores. Furthermore, Falcon Heavy utilizes the same
second stage and same payload fairing as flown on Falcon 9, fully
benefitting from the flight heritage provided by Falcon 9 flights. This
commonality has also minimized infrastructure unique to the vehicle.
SpaceX first launched the Falcon Heavy vehicle in February of 2018.


The first stage comprises three cores: a center core and two side boosters (the first stage of Falcon 9 is used as a side
booster); each core has nine Merlin 1D (M1D) engines. Each of the 27 first-stage engines produces 190,000 lbf of thrust
at sea level, for a total of 5,130,000 lbf of thrust at liftoff. The two side boosters are connected to the center core at the
base engine mount and at the forward end of the LOX tank on the center core.

With nine engines in each first-stage core, Falcon Heavy has propulsion redundancy – unlike any other heavy-lift launch
system. The launch vehicle monitors each engine individually during ascent and can, if necessary, preemptively
command off-nominal engines, provided the minimum injection success criteria are achievable with the remaining
engines. This engine-out reliability provides propulsion redundancy throughout first-stage ascent – a feature unique to
Falcon launch vehicles.


The first-stage propellant tank walls of the Falcon vehicles are made from an aluminum lithium alloy. Tanks are
manufactured using friction stir welding—the highest strength and most reliable welding technique available. A common
dome separates the LOX and RP-1 tanks, and a double-wall transfer tube carries LOX through the center of the RP-1 tank
to the engine section. Four grid fins near the top of the first stage along with four deployable legs at the base are
nominally flown to support recovery operations.

Nine SpaceX Merlin engines power the Falcon 9 first stage with up to 854 kN (1 9 0,000 lbf) thrust per engine at sea level,
for a total thrust of 7,686 kN (1. 71 million lbf) at liftoff. The first-stage engines are configured in a circular pattern, with
eight engines surrounding a center engine.

Twenty-seven SpaceX Merlin engines power the Falcon Heavy first stages for a total thrust of 5,130,000 lbf at liftoff. The
figure below shows the nomenclature for the center core and side boosters (center, plus y-axis and minus y-axis.)
Structurally, the plus y-axis and minus y-axis boosters are identical. The center core consists of thicker tank walls and
carries the booster separation system. The z axis points to zenith when the vehicle is horizontal.

After engine start, Falcon vehicles are held down until all vehicle systems are verified as functioning normally before
release for liftoff.

The Falcon vehicles’ interstage, which connects the first and second stages, is a composite structure consisting of an
aluminum honeycomb core surrounded by carbon fiber face sheet plies. The interstage is fixed to the forward end of the
first-stage tank. The stage separation system is located at the forward end of the interstage and interfaces to the second-
stage.

The second-stage tank for Falcon vehicles is a shorter version of the first-stage tank and uses most of the same
materials, construction, tooling and manufacturing techniques as the first-stage tanks. A single Merlin Vacuum (MVac)
engine powers the second stage, using a fixed 1 65 :1 expansion nozzle. For added reliability of restart, the engine contains
dual redundant triethylaluminum-triethylborane (TEA-TEB) pyrophoric igniters. In addition, the second stage contains a
cold nitrogen gas (GN 2 ) attitude control system (ACS) for pointing and roll control. The GN 2 ACS is more reliable and
produces less contamination than a propellant-based reaction control system.


```
Characteristic First Stage Core Second Stage
Structure
Height 70 m (229 ft) including both stages, interstage and standard fairing; 75.2 m (2 4 6.
ft) with extended fairing.
Diameter 3.66 m (12 ft) 3.66 m (12 ft)
Type LOX tank – monocoque
Fuel tank – skin and stringer
```
```
LOX tank – monocoque
Fuel tanks – skin and stringer
Material Aluminum lithium skin; aluminum domes
Propulsion
Engine type Liquid, gas generator Liquid, gas generator
Engine designation M1D MVac
Engine designer SpaceX SpaceX
Engine manufacturer SpaceX SpaceX
Number of engines 9 1
Propellant Liquid oxygen/kerosene (RP-1) Liquid oxygen/kerosene (RP-1)
Thrust (stage total) 7,686 kN (sea level) (1, 71 0,000 lbf) 981 kN (Vacuum) (220,500 lbf)
Propellant feed system Turbopump Turbopump
Throttle capability Yes (1 9 0,000 lbf to 108,300 lbf sea level) Yes (220,500 lbf to 140,679 lbf)
Restart capability Yes Yes
Tank pressurization Heated helium Heated helium
Ascent attitude control
Pitch, yaw Gimbaled engines Gimbaled engine/nitrogen gas
thrusters
Roll Gimbaled engines Nitrogen gas thrusters
Coast attitude control Nitrogen gas thrusters
(recovery only)
```
```
Nitrogen gas thrusters
```
```
Operations
Shutdown process Commanded shutdown Commanded shutdown
Stage separation system Pneumatically actuated
separation mechanism
```
### N/A

The first and second stages are mated by mechanical latches at three points between the top of the interstage and the
base of the second-stage fuel tank. After the first-stage engines shut down, a high-pressure helium circuit is used to
release the latches via redundant actuators. The helium system also preloads four pneumatic pushers, which provide a
positive-force for stage separation after latch release. This includes a redundant center pusher to further decrease the
probability of re-contact between the stages following separation.

The two halves of the standard fairing are fastened by mechanical latches along the fairing vertical seam. To deploy the
fairing, a high-pressure helium circuit releases the latches, and four pneumatic pushers facilitate positive-force
deployment of the two halves. The use of all-pneumatic separation systems provides a benign shock environment,
allows acceptance and preflight testing of the actual separation system hardware, and minimizes debris created during
separation.

The two halves of the extended fairing are fastened by a bolted frangible seam joint. To deploy the fairing, redundant
detonators initiate a detonation cord contained inside an expanding tube assembly. The detonation causes the
expanding tube to expand outwards and break the structural seam between the two fairings in a controlled and
contained manner. Four pneumatic pushers facilitate positive-force deployment of the two halves. The use of a non-
bolted clamshell interface between the payload fairing and the rest of the vehicle provides significant shock attenuation
of the separation event, maintaining environments for the payload well within nominal payload requirements.


For Falcon Heavy, the fundamental purpose of the side cores is to apply axial force to the center core during ascent and
increase the impulse delivered to second stage before stage separation. The timing of the shutdown for the Falcon
Heavy side cores can be tailored for each mission to ensure that the proper impulse is delivered. Each side core is
structurally connected to the center core at forward and aft locations. Two pneumatic pusher separation mechanisms
connect the forward ends of each side core to the center core, fastening the top of the LOX tank in the center core to the
side cores. They maintain the connection during ascent and then actively jettison the side cores following side core
shutdown. Two identical pusher separation mechanisms connect the aft ends of each side core to the center core and
are used to laterally force the base of the side cores from the center core following the side core shut down.

Falcon avionics feature a flight-proven, three-string, fault-tolerant architecture that has been designed to human-rating
requirements. Avionics include flight computers, Global Positioning System (GPS) receivers, inertial measurement units,
SpaceX-designed and manufactured controllers for vehicle control (propulsion, valve, pressurization, separation and
payload interfaces), a network backbone, S-band transmitters and a C-band transponder for range safety tracking. The
S-band transmitters are used to transmit telemetry and video to the ground, from both the first and second stages, even
after stage separation.

Our launch vehicles are equipped with an autonomous flight termination system (AFTS) to limit the potential damage
caused by a launch vehicle malfunction. The system terminates the flight of the vehicle automatically if mission rules
are violated. The use of an AFTS requires fewer range assets to support launch operations, resulting in fewer range
constraints and increased launch opportunities.

Falcon vehicles use a right-hand X-Y-Z coordinate frame centered 440.69 cm (173.5 in.) aft of the first-stage radial engine
gimbal, with +X aligned with the vehicle long axis and +Z opposite the transporter-erector strongback (Figure 2 - 4 ). X is
the roll axis, Y is the pitch axis, and Z is the yaw axis. Additional coordinate frames may be defined with reference to the
payload interface (Section 5.1.1) for specific missions.


SpaceX launch services are offered at its Cape Canaveral Space Force Station, Kennedy Space Center, and Vandenberg
Space Force Base launch sites. Together, Cape Canaveral Space Force Station and Kennedy Space Center are referred
to herein as the Eastern Range. Additional launch facilities are currently under development in South Texas (Section 6 ).

Table 3 - 1 describes the typical injection orbits available from our operational launch sites. (As other launch sites are
activated, this User’s Guide will be updated.)

```
Insertion Orbit Inclination Range Vehicle Launch Site(s)
LEO 28.5 – 55 deg Falcon 9 or Falcon
Heavy
```
```
Eastern Range
```
```
LEO 55 – 66 deg Falcon 9 Vandenberg
LEO polar/
SSO
```
```
66 – 145 deg Falcon 9 Vandenberg or
Eastern Range
GTO Up to 28.5 deg Falcon 9 or Falcon
Heavy
```
```
Eastern Range
```
```
GSO Up to 28.5 deg Falcon Heavy Eastern Range
Earth escape N/A Falcon 9 or Falcon
Heavy
```
```
Vandenberg or
Eastern Range
```
Launch services to a range of low Earth orbits are available, including services to low-inclination orbits through high-
inclination and sun-synchronous orbits (SSO). Falcon vehicles can provide either two-burn or direct-inject launch
services: two-burn mission profiles optimize vehicle performance, while direct-inject mission profiles offer reduced
mission duration and require only a single start of the second-stage engine. LEO missions to a 55 deg inclination or lower
are flown from the Eastern Range (with a performance penalty between 53 and 55 deg due to the need to perform a “dog
leg” maneuver); LEO missions to higher inclinations are baselined to be flown from Vandenberg Space Force Base, but
may also be flown from the Eastern Range in specific cases and at SpaceX’s discretion (contact SpaceX for more
information). Launch services to inclinations lower than 28.5 deg are available from the Eastern Range, but they incur a
performance penalty.

Launch services to a range of GTOs and other high-altitude orbits are available, including standard GTO, sub-GTO for
heavy payloads, and supersynchronous injection. A perigee altitude of 185 km (100 nmi) is baselined for GTO; higher
perigee values may be provided with a performance penalty. Currently, all GTO missions are flown from the Eastern
Range.

Launch services directly into geosynchronous orbit (GSO) are available from Kennedy Space Center via Falcon Heavy.
The satellite is placed into a circular orbit directly above or below GSO to allow it to phase into its correct orbital position.

Launch services to a range of Earth escape orbits are available. Customers may also utilize a customer-supplied kick-
stage to achieve higher escape energy (C3) performance, based on mission requirements. Earth escape missions are
typically flown from the Eastern Range.

Mass-to-orbit capabilities for the Falcon 9 and Falcon Heavy fairing configuration are available upon request.


The baseline SpaceX payload attach fitting (PAF) shown in Figure 3 - 1 converts the diameter of the launch vehicle to a
(typical) standard 1, 575 - mm (62.01 in.) bolted interface. SpaceX also offers a PAF with a 2, 624 - mm (103.307 in.) bolted
interface (Figure 3 - 2 ). SpaceX can also provide a PAF with a wider interface. Please contact SpaceX for more details.

Payloads should comply with the mass properties limitations given in Figure 3 - 3 (for the 1575-mm PAF) and Figure 3 - 4
(for the 2624-mm PAF). Payloads in excess of these figures can be accommodated as a mission unique service. Payload
mass properties should be assessed for all items forward of the PAF 1575 - mm or 2624-mm bolted interfaces (Section
5.1.1), including any mission-unique payload adapters and separation systems. Mass properties capabilities may be
further constrained by mission-unique payload adapters, dispensers or separation systems.


SpaceX requires that customers verify the mass properties of their system through measurement before shipping it to
the launch site. SpaceX may request insight into relevant analyses and testing performed for satellite qualification,
acceptance and interface verification. Falcon vehicles may be able to accommodate payloads with characteristics
outside the limitations indicated in this section. Please contact SpaceX with your mission-unique requirements.

-

```
0
```
```
1000
```
```
2000
```
```
3000
```
```
4000
```
```
5000
```
```
6000
```
```
7000
```
```
Payload CG Height from SIS Interface [mm]^020004000600080001000012000
Payload Mass, including Adapter [kg]
```
**Falcon 1,575 PAF Capability**


Falcon launch vehicles can launch any day of the year, at any time of day, subject to environmental limitations and
constraints as well as range availability and readiness. Launch window times and durations are developed specifically
for each mission. Customers benefit from recycle operations, maximizing launch opportunities within the launch window
(Section 8.5.6).

Falcon 9 and Falcon Heavy can provide payload pointing and roll control during long-duration coast phases for sun
avoidance and thermal control. If requested, the Falcon second stage will point the X-axis of the launch vehicle to a
customer-specified attitude and perform a passive thermal control roll of up to ±1.5 deg/sec around the launch vehicle
X-axis, held to a local vertical/local horizontal (LVLH) roll attitude accuracy of ±5 deg.

Falcon launch vehicles offer 3 - axis attitude control or spin-stabilized separation as a standard service. For inertial
separation, the vehicle will point the second stage and payload to the desired LVLH attitude and minimize attitude rates.
For spin-stabilized separation, the Falcon launch vehicle will point the second stage and payload to the desired LVLH
attitude and initiate a spin about the launch vehicle X-axis at a customer-specified rate dependent upon payload mass
properties. Standard pre-separation attitude and rate accuracies are developed as a mission-specific standard service.
More information about separation attitude and rate accuracy is available from SpaceX upon request.

Falcon 9 and Falcon Heavy can launch multiple satellites on a single mission, with the customer responsible for the
integration of the multiple payloads. As a liquid-propellant launch vehicle with restart capability, Falcon launch vehicles
also provide the flexibility to deploy each satellite into a different orbit, performance allowing. SpaceX also offers
dedicated rideshare missions via its Smallsat Rideshare Program.

Falcon launch vehicles can accommodate a broad range of dispenser systems including multi-payload systems and
mission-unique adapters. SpaceX can develop and provide such adapters and dispensers if desired, as a nonstandard
service, or can integrate third-party systems. Please contact SpaceX with your mission-unique requirements.

SpaceX typically reserves the right to manifest secondary payloads aboard Falcon missions on a non-interference basis.
Secondary payloads may be manifested on a variety of secondary payload adapters including a SpaceX-developed
Rideshare Dispenser ring, a SpaceX-developed Surfboard, or other mission-unique secondary deployment structures.

Please contact SpaceX or refer to the Rideshare Payload User's Guide for information regarding flight opportunities,
interface requirements and pricing for secondary payloads.


Falcon 9 and Falcon Heavy have been designed to provide as benign a payload environment as possible, via the use of
all-liquid propulsion, a single staging event, deeply throttleable engines and pneumatic separation systems. The
environments presented below reflect typical mission levels for Falcon 9 and Falcon Heavy, and are based on the use of
the standard fairing; please contact SpaceX for more information on payload environments for missions requiring the
extended fairing. Mission-specific analyses will be performed and documented in an interface control document for each
contracted mission.

SpaceX recommends using the quasi-static limit load factors provided by NASA-HDBK-7005 (Table 4 - 1 ). SpaceX has
quantified the maximum predicted environments experienced by the payload during transportation. Transportation will
be accomplished by two wheeled vehicles: a payload transporter from the payload processing facility to the hangar, and
the launch vehicle transporter-erector from the hangar to the launch pad. It is expected that transportation environments
will be enveloped by the flight environments in Section 4.3.

```
Transportation Method
```
```
Longitudinal
Load (g)
```
```
Lateral
Load (g)
```
```
Vertical
Load^2 (g)
Slow-moving dolly (expected ground transport loads) ± 1.0 ± 0.75 ± 2.
```
The standard service temperature, humidity and cleanliness environments during various processing phases are
provided in Table 4 - 2. SpaceX can accommodate environments outside the standard service. Please contact SpaceX for
details.

Conditioned air will be disconnected for a short duration during rollout to the pad. Spacecraft environmental
temperatures will be maintained above the dew point of the supply air at all times. A nitrogen purge is available as a
nonstandard service. The PAF and fairing surface are cleaned to Visibly Clean-Highly Sensitive, achieving a residue level
between A/5 and A/2 and particulate between 300- 500 micron, per IEST-STD-CC1246D.

```
Phase Control System
```
```
Approx.
Duration Temp. °C (°F) Humidity
```
```
Cleanliness
(class)
```
```
Flow
Rate
(cfm)
Spacecraft
processing
```
```
Payload
processing
facility heating,
ventilation and air
conditioning
(HVAC)
```
```
3 weeks 21 ± 3 (70 ± 5) CCSFS/KSC:
45% ± 15%
VSFB:
50% ± 15%
```
### 100,

```
(Class 8)
```
### N/A

```
Propellant
conditioning
```
```
Facility HVAC 3 days 21 ± 3 (70 ± 5) CCSFS/KSC:
45% ± 15%
VSFB:
50% ± 15%
```
### 100,

```
(Class 8)
```
### N/A

(^2) Vertical direction defined with respect to the gravity vector.


```
Phase Control System
```
```
Approx.
Duration Temp. °C (°F) Humidity
```
```
Cleanliness
(class)
```
```
Flow
Rate
(cfm)
Spacecraft
propellant
loading
```
```
Facility HVAC Mission-
Unique
```
### 21 ± 3 (70 ± 5) CCSFS/KSC:

### 45% ± 15%

### VSFB:

### 50% ± 15%

### 100,

```
(Class 8)
```
### N/A

```
Transport from
SpaceX
Payload
Processing
Facility to
hangar
(CCSFS/KSC
only)
```
```
Transport trailer
unit
```
```
< 6 hrs 21 ± 3 (70 ± 5) 0%-60% 10,
(Class 7)
(supply air
cleanliness)
```
### 1,

```
Encapsulated
in hangar
```
```
Ducted supply
from hangar
facility HVAC
```
```
1 week 21 ± 3 (70 ± 5) CCSFS/KSC:
45% ± 15%
VSFB:
50% ± 15%
```
### 10,

```
(Class 7)
(supply air
cleanliness)
```
### 1,

```
Encapsulated
roll-out to pad
```
```
None 30 - 60 min N/A N/A 10,
(Class 7
supply air
cleanliness)
```
### N/A

```
Encapsulated
on pad (vertical
or horizontal)
```
```
Pad air
conditioning
```
```
<1 day VSFB:
Selectable 15 to
35 (59 to 95)
CCSFS: Selectable
16 to 30 (61 to 86)
```
```
0% to 65% 10,
(Class 7 )
(supply air
cleanliness)
```
### 1,

The maximum predicted environments the payload will experience from liftoff through separation are described in the
sections below. Falcon vehicles may be able to accommodate payloads with characteristics outside the limitations
indicated in these sections and may also be able to provide environments lower than those indicated in these sections.
Please contact SpaceX with your mission-unique requirements.

During flight, the payload will experience a range of axial and lateral accelerations. Axial acceleration is driven by vehicle
thrust and drag profiles; lateral acceleration is primarily driven by wind gusts, engine gimbal maneuvers, first-stage
engine shutdown and other short-duration events. Both the first- and second-stage engines may be throttled to help
maintain launch vehicle and payload steady state acceleration limits.

For “standard” payloads with mass of more than 4,000 lb (1,810 kg), Falcon 9 and Falcon Heavy payload design load
factors are shown using the envelope in Figure 4 - 1. For “light” payloads with mass of less than 4,000 lb (1,810 kg), Falcon
9 load factor is provided in Figure 4 - 2. For Falcon Heavy “light” payloads, please contact SpaceX for more details.
Provided loads are maximum flight loads (limit level) and do not contain a qualification factor.

The load factors provided below are intended for a single payload mission; multi-payload missions should coordinate
directly with SpaceX. A positive axial value indicates a compressive net-center-of-gravity acceleration, while a negative
value indicates tension. Actual payload loads, accelerations and deflections are a function of both the launch vehicle and
payload structural dynamic properties and can be accurately determined via a coupled loads analysis.


Payloads should consider maintaining the primary lateral frequency above 10Hz, primary axial frequency above 25Hz,
and all secondary structure minimum resonant frequencies above 35Hz to avoid interaction with launch vehicle
dynamics.

The Falcon 9 and Falcon Heavy design load factors provided below are for typical spacecraft above 4,000 lb, and are
applicable to mission that use either the 1, 575 - mm or the 2, 624 - mm PAF. Please consult with SpaceX for applicability
based on spacecraft modal frequencies and CG height.

Figure 4 - 2 shows the Falcon 9 design load factors for lighter payloads (less than 4,000 lb). However, for ultra-light
payloads (~2,000 lb or less), coordination with SpaceX mission management is required, since these load factors may
not be adequate to design the payload. Actual spacecraft loads, accelerations and deflections are a function of both the
launch vehicle and payload structural dynamic properties and can only be accurately determined via a coupled loads
analysis.

0.5, 6

```
0.5, 4
2, 3.5
```
2, -1.5

0.5, -1.5

```
0.5, - 2
-3
```
-2

-1

0

1

2

3

4

5

6

7

-3 -2 -1 0 1 2 3

**Axial Acceleration (g)**

**Lateral Acceleration (g)**


Please contact SpaceX for more information.

Maximum predicted sinusoidal vibration environments represent the levels at the top of the payload attach fitting for
Q=20 through Q=50, and envelope all stages of flight. Maximum predicted sinusoidal vibration environments for Falcon
9 and Falcon Heavy are shown in Figure 4 - 3 and Figure 4 - 4. These environments represent the vibration levels at the top
of the PAF for Q=20 through Q=50, and envelope all stages of flight. Provided loads are maximum flight loads (limit level)
and do not contain a qualification factor. Since SpaceX accommodates a variety of payloads, results of coupled loads
analysis will be used to modify these levels, if necessary, to reflect the levels at the payload interface.

2, 8.5

2, 4 3, 4

```
3, -1.5
2, -1.5
```
2, - 4

-6

-4

-2

0

2

4

6

8

10

-4 -3 -2 -1 0 1 2 3 4

**Axial Acceleration (g)**

**Lateral Acceleration (g)**

F9 Design Load Factors F9 Design Load Factors, Payloads < 4,000 lb


```
0
```
```
0.1
```
```
0.2
```
```
0.3
```
```
0.4
```
```
0.5
```
```
0.6
```
```
0.7
```
```
0.8
```
```
0.9
```
```
1
```
```
0 10 20 30 40 50 60 70 80 90 100
```
**Acceleration (g)**

```
Frequency (Hz)
```
```
Frequency (Hz)
5
85
100
```
```
Acceleration (g)
0.5
0.5
0.6
```
```
Applicable for Q 20
```

During flight, the payload will be subjected to a varying acoustic environment. Levels are highest near liftoff and during
transonic flight, due to aerodynamic excitation. The acoustic environment, defined as the spatial average and derived at
a P95/50 level, is shown by both full-octave and third-octave curves.

Figure 4 - 5 and Table 4 - 3 provide the Falcon 9 third-octave maximum predicted acoustic environment for typical
payloads, while Figure 4 - 6 and Table 4 - 4 provide the full-octave maximum predicted acoustic environment. Levels are
shown for both Cape Canaveral (SLC-40 and LC-39A) and Vandenberg (SLC-4E) launch sites respectively, and are based
on the use of the SpaceX standard fairing with acoustic blankets installed.

The acoustic maximum predicted environment for typical payloads in the SpaceX standard fairing with no acoustic
blankets installed is shown in Figure 4 - 7 and Table 4 - 5 (third octave) and Figure 4 - 8 and Table 4 - 6 (full-octave).

Predicted acoustic levels for a specific mission will depend on the use of acoustic blankets and the payload’s size and
volume, with smaller payloads generally having lower acoustic levels. Margin for qualification testing or for payloads
larger than 60% volume fill is not included in the curves below.


Frequency (Hz)

```
Cape Canaveral Acoustic Limit
Levels (P95/50), 60% Fill-
Factor (Third-Octave)
```
```
Vandenberg Acoustic Limit
Levels (P95/50), 60% Fill-
Factor (Third-Octave)
31.5 118 119.75
40 119.5 120
50 120 120
63 120 120
80 119.8 119.8
100 120.5 120.5
125 121.5 121 .5
160 122 122
200 121.5 121.5
250 120.5 120.5
315 119 119
400 117 117
500 115 115
630 113 113
800 111 111
1000 109.5 109.5
1250 108 108
1600 107 107
2000 106 106
2500 105 105
3150 104 104
4000 103 103
5000 102 102
6300 101 101
8000 100 100
10000 99 99
OASPL (dB) 131. 3 131. 4
```

Frequency (Hz)

```
Cape Canaveral Acoustic
Limit Levels (P95/50), 60%
Fill-Factor (Full Octave)
```
```
Vandenberg Acoustic Limit
Levels (P95/50), 60% Fill-
Factor (Full Octave)
31.5 122.4 124.1
63 124.7 124.7
125 126.1 126.1
250 125.2 125.2
500 120.1 120.1
1000 114.4 114.4
2000 110.8 110.8
4000 107.8 107.8
8000 104.8 1 04.8
OASPL (dB) 131.4 131.6
```


Frequency (Hz)

```
Cape Canaveral Acoustic Limit
Levels (P95/50), 60% Fill-
Factor (Third-Octave)
```
```
Vandenberg Acoustic Limit
Levels (P95/50), 60% Fill-
Factor (Third-Octave)
```
31.5 (^118) 120.5
(^40) 119.5 121.5
(^50 120 122)
(^63 120) 122.5
(^80 121) 123.5
(^100) 123.3 124.5
(^125) 127.7 127.7
(^160) 129.3 129.3
(^200 1) 29.8 129.8
(^250) 129.5 129.5
(^315 128 128)
(^400 126 126)
(^500 124 124)
(^630 122 122)
(^800) 119.5 119.5
(^1000) 117.8 117.8
(^1250) 116.4 116.4
(^1600) 114.5 114.5
(^2000 113 113)
(^2500) 111.3 111.3
(^3150) 110.2 110.2
(^4000 109 109)
(^5000) 107.5 107.5
(^6300 106 106)
(^8000 104 104)
(^10000 102 102)
OASPL (dB) (^) 137.6 137.9


Frequency (Hz)

```
Cape Canaveral Acoustic
Limit Levels (P95/50), 60%
Fill-Factor (Full Octave)
```
```
Vandenberg Acoustic Limit
Levels (P95/50), 60% Fill-
Factor (Full Octave)
```
31.5 (^) 122.4 125.2
(^63) 125.1 127.5
(^125) 132.2 132.4
(^250) 133.9 133.9
(^500) 129.1 129.1
(^1000) 122.9 122.9
(^2000) 117.9 117.9
(^4000) 113.8 113. 8
(^8000) 109.1 109.1
OASPL (dB) (^) 137.6 137.9


Figure 4 - 9 and Table 4 - 7 provide the Falcon Heavy third-octave maximum predicted acoustic environment for typical
payloads, while Figure 4 - 10 and Table 4 - 8 provide the full-octave maximum predicted acoustic environment. These levels
are applicable to launches from Cape Canaveral (LC-39A). Predicted acoustic levels for a specific mission will depend
on the payload’s size and volume with smaller payloads generally having lower acoustic levels. Margin for qualification
testing or for payloads larger than 60% volume fill is not included in the curves below.


Frequency (Hz) Acoustic Limit Levels (P95/50),
60% Fill-Factor (Third-Octave)
31.5 125
40 126 .5
50 1 26.5
63 1 25.5
80 125
100 1 24.5
125 124
160 1 23.5
200 123
250 122
315 12 0.5
400 1 18.5
500 1 16.5
630 114 .5
800 112
1000 1 09.5
1250 108
1600 107
2000 106
2500 105
3150 104
4000 103
5000 102
6300 101
8000 100
10000 99
OASPL (dB) 1 35.2


```
Frequency
Acoustic Limit Levels (P95/50),
60% Fill-Factor (Full Octave)
31.5 13 0.3
63 13 0.5
125 1 28.8
250 1 26.7
500 12 1.6
1000 11 4.9
2000 11 0.8
4000 1 07.8
8000 10 4.8
```
OASPL (dB) 1 35.6


Five events during flight result in loads that are characterized as shock loads:

1. Release of the launch vehicle hold-down at liftoff.
2. Booster separation (Falcon Heavy only).
3. Stage separation.
4. Fairing deployment.
5. Spacecraft separation.

Of these events, the first three are negligible for the payload relative to fairing deployment and spacecraft separation
because of the large distance and number of joints over which the shocks will travel and dissipate. The maximum shock
environment predicted at the 1, 575 - mm interface for fairing deployment is enveloped by the shock environment from
typical spacecraft separation. Consequently, the shock environment is typically a function of the spacecraft adapter and
separation system selected for the mission. Actual shock environments experienced by the payload at the top of the
mission-unique payload adapter will be determined following selection of a specific payload adapter and separation
system. Table 4 - 9 shows typical payload adapter-induced shock at the spacecraft separation plane for 937-mm or 1, 194 -
mm or 1 ,666 mm (36.89 in. or 47.01 in. or 65.59 in.) clampband separation systems, derived at a P95/50 statistical level.
Please note the actual flight shock levels produced by the payload adapter will be mission-unique.

```
Frequency (Hz) SRS (g)
100 30
1000 1 , 000
10000 1 , 000
```
The maximum predicted random vibration environment at the top of the PAF can be seen in Figure 4 - 11 and Table 4 - 10.
This environment is derived from flight data measured at the top of the PAF and does not account for any additional
attenuation as the vibration traverses the mission-specific payload adapter or spacecraft interface. The smoothline is
an envelope of all flight events (liftoff, Stage 1 ascent, and S2 burns) and is derived at a P95/50 statistical level.

The random vibration environment is derived from the maximum response due to multiple forcing functions. These
forcing functions can be broken into three frequency bins as shown in Figure 4 - 12 and listed below:

1. Low Frequency (0 – 100Hz)
    a. Excitations driven by global vehicle motion and modes
    b. CLA and sine vibration envelope this region
2. Mid Frequency (100Hz – 600Hz)
    a. Excitation due to aeroacoustics
    b. Acoustic excitation and aero buffet are primary drivers in this region
3. High Frequency (600Hz – 2000Hz)
    a. Excitation due to structure-borne vibration
    b. MVac forcing functions

Spacecraft complying with standard component-level qualification practices such as GEVs or SMC-S-016 are generally
covered for this environment. Spacecraft with sensitive components that are not screened to vibration levels above the
Falcon MPE can assess if acoustic testing envelopes the random vibration environment. One approach to determine
this is to measure acceleration responses near components during acoustic testing. Components closer to the
spacecraft separation plane are more likely to be driven by random vibration as opposed to acoustics than those further
away. Spacecraft components with high surface area to mass ratios such as photovoltaic arrays generally see higher


excitations from acoustic environments than from random vibration. However, these criteria are subjective and
engineering best judgement should be used.

```
Frequency
Falcon 9/Heavy Payload
Vibration MPE, (P95/50),
5.13 GRMS
20 0.0044
100 0.0044
300 0.01
700 0.01
800 0.0 3
925 0.0 3
2000 0.0 0644
GRMS 5.13
```

Spacecraft with sensitive components not screened with standard-level qualifications (GEVS or SMC-S-016) may require
additional relief from random vibration. SpaceX offers random vibration attenuation as a nonstandard service. For
programmatic information, please reach out to SpaceX directly.

Falcon launch vehicles include several radio frequency (RF) systems, which are summarized in Table 4 - 11 for Falcon 9
and Table 4 - 12 for Falcon Heavy.


```
Part Description TX/RX(ReceiverTransmitter/ ) Frequency (MHz) 99% Bandwidth (MHz) Modulation
S1TX1 Telemetry Transmitter
TX
```
22 47.5 (^) 4.84
PCM/FM
S1TX2 Telemetry Transmitter 2255.5
S2TX1 Telemetry Transmitter 2232.5
S2TX2 Telemetry Transmitter 2272.5 4.1^4
GPS Receiver RX 1575.42 20 BPSK DSSS
Iridium/GPS Tracker TX 1610 - 1626.5 0.042 BPSK/QPSK
Iridium/GPS Tracker RX 1610 - 1626.5 0.042 QPSK
Iridium/GPS Tracker RX 1575.42 20 BPSK DSSS
S-Band BPSK Receiver RX 2090 - 2093 1 BPSK
Radar Altimeter TX 4235 - 4275 40 FMCW
Radar Altimeter TX 4325 - 4365 40 FMCW
Radar Altimeter TX 4250 - 4350 100 FMCW
Radar Altimeter RX 4235 - 4275 40 FMCW
Radar Altimeter RX 4325 - 4365 40 FMCW
Radar Altimeter RX 4250 - 4350 40 FMCW
Part Description TX/RX(ReceiverTransmitter/ ) Frequency (MHz) 99% Bandwidth (MHz) Modulation
S1TX1 Telemetry Transmitter

### TX

22 47.5 (^) 4.84
S1TX2 Telemetry TransS2TX1 Telemetry Transmittermitter 2255.52232.5 (^) PCM/FM
S2TX2 Telemetry Transmitter 2272.5 4.14^
SB1TX Telemetry Transmitter 2370.5 (^) 4.88 SOQPSK
SB2TX Telemetry Transmitter 2382.5
GPS Receiver RX 1575.42 20 BPSK DSSS
Iridium/GPS Tracker TX 1610 - 1626.5 0.042 BPSK/QPSK
Iridium/GPS Tracker RX 1610 - 1626.5 0.042 QPSK
Iridium/GPS Tracker RX 1575.42 20 BPSK DSSS
S-Band BPSK Receiver RX 2090 - 2093 1 BPSK
Radar Altimeter TX 4235 - 4275 40 FMCW
Radar Altimeter TX 4325 - 4365 40 FMCW
Radar Altimeter TX 4212.5-4252.5 40 FMCW
Radar Altimeter TX 4302.5-4342.5 40 FMCW
Radar Altimeter TX 4257.5-4297.5 40 FMCW
Radar Altimeter TX 4347.5-4387.5 40 FMCW
Radar Altimeter RX 4235 - 4275 40 FMCW
Radar Altimeter RX 4325 - 4365 40 FMCW
Radar Altimeter RX 4212.5- 4252 .5 40 FMCW
Radar Altimeter RX 4302.5-4342.5 40 FMCW
Radar Altimeter RX 4257.5-4297.5 40 FMCW
Radar Altimeter RX 4347.5-4387.5 40 FMCW
Payload customers must ensure that payload materials or components sensitive to RF environments are compatible
with the worst-case Falcon 9 (Figure 4 - 13 and Table 4 - 13 ) and Falcon Heavy (Figure 4 - 14 and Table 4 - 14 ) launch vehicle
radiated environment. These limits envelope expected emissions as calculated at the plane between the PAF and


mission-specific payload adapter and do not include EMI safety margin or emissions from Avionics inside the fairing.
Emissions from Avionics located inside the fairing volume are provided in Section 4.3.6.4. Notch requests will be
assessed for compatibility on a mission-specific basis; notches for spacecraft receivers can typically be accommodated
to the fairing avionics emissions envelope ( 48 dBuV/m) or lower depending on clearances to the payload dynamic
envelope.

```
Frequency Range (MHz) E Field Limit (dBμV/m) Launch Vehicle
Transmit System
1.00 – 2200.0 90
2200.0 – 2300.0 140 S-band telemetry and video
2300.0 – 18000.0 90
```

```
Frequency Range
(MHz)
```
```
E Field Limit
(dBμV/m)
```
```
Launch Vehicle
Transmit System
1.00 – 2200.0 90
2200.0 – 2300. 0 140 S-band telemetry and video
2300.0 – 2360.0 90
2360.0 – 2395 .0 140 S-band telemetry and video
2395 .0 – 18000.0 90
```
Maximum spacecraft emissions for Falcon 9 and Falcon Heavy are shown in Figure 4 - 15 and Table 4 - 15. Payloads
should not emit radiation in excess of the maximum allowable spacecraft emissions at any time during processing,
integration or flight, as measured at the top of the PAF. Standard Falcon services do not permit active payload radiation
during the countdown or flight prior to separation from the second stage. This limit envelopes expected emissions as
calculated at the plane between the PAF and mission-specific payload adapter and includes EMI safety margin. Notch
requests will be assessed for compatibility on a mission-specific basis; notches for spacecraft transmitters can typically
be accommodated to a level that is 6dB lower than SpaceX Avionics qualification limits. Please consult with SpaceX for
your mission-unique requirements.


```
Frequency Range (MHz) E Field Limit
(dBμV/m)
```
```
Launch Vehicle
Receive System
1.0 – 1565.42 120.0
```
1565. 42 – 1585. 42 48 .0 GPS L1
    1585. 42 – 2090.0 120.0
       2090.0 – 2093.0 70 .0 Stage 1 Telecommand
    2093.0 – 18000.0 120.0

Falcon launch vehicles have avionics inside the fairing. The fairing emission level is shown in Figure 4 - 16 and Table 4 - 16.
This limit envelopes the maximum expected combined emissions from these avionics, as calculated at the surface of
the payload volume defined in Figure 12 - 5 in Appendix A. EMI safety margin is not included.


```
Frequency Range
(MHz)
```
```
E Field Limit
(dBμV/m)
30.0 – 18000 .0 80
```
SpaceX has launch facilities on the East coast (SLC-40 and LC-39A) and on the West coast (SLC-4E). This limit envelopes
the expected emissions at all SpaceX integration and launch facilities, including Range sources, local radar systems, and
communications systems in use at SpaceX facilities (WiFi, mobile phones, two-way radios, etc.). Spacecraft designed
and tested to this limit (plus appropriate safety margin) can expect to be compatible with all known launch site emissions
between spacecraft arrival and delivery to orbit. The envelope is calculated at the surface of the spacecraft and EMI
safety margin is not included.

Site-specific (not enveloped) analysis will be performed on a mission-specific basis as needed to meet customer
requirements. Notches for spacecraft receivers typically do not overlap with launch site emissions frequencies and can
typically be accommodated.


```
Frequency Range
(MHz)
```
```
E Field Limit
(dBμV/m)
100 – 400 132
400 – 1200 140
1200 – 1400 148
1400 – 11000 146
11000 – 18000 90
```
To account for unexpected variation in hardware and environments, 6dB of EMI safety margin is required. EMI safety
margin is typically expected to be included on the “victim” side of the source-victim analysis. Each emissions section in
this guide specifies whether safety margin has been included in the envelope provided. When safety margin has not
been included, it is expected that the relevant spacecraft susceptibility limit will include 6dB of EMI safety margin.

SpaceX launch pads at CCSFS/KSC contain full lightning protection systems. The integration facilities and hangars are
equipped with lightning grounding systems to protect personnel and hardware from lightning. The SLC- 40 and LC-39A
launch pads are equipped with overhead wire lightning protection systems. These systems are designed to:

1. Be a preferential path for lightning in order to prevent direct attachments to personnel and hardware in the
    protection zone.
2. Avoid side flash between the overhead wires and flight hardware and ground systems.
3. Minimize electromagnetic coupling to flight hardware and ground systems in order to protect sensitive
    electronics.


Well-defined lightning retest criteria are important to minimize both the risk of damage and the risk of missed launch
opportunities for spacecraft and launch vehicles. As such, Falcon launch vehicles have well-defined lightning retest
criteria that are based on the lightning distance and amplitude data measured using range-provided lightning monitoring
systems. SpaceX requires spacecraft to provide lightning retest criteria based on lightning strike distance and amplitude.

Inside the Falcon launch vehicle, the payload fairing internal pressure will decay at a rate no larger than 0. 40 psi/sec (2. 8
kPa/sec) from liftoff through immediately prior to fairing separation, except for brief periods during flight, where the
payload fairing internal pressure will decay at a rate no larger than 0.65 psi/sec (4.5 kPa/sec), for no more than 5
seconds.

The SpaceX payload fairing is a composite structure consisting of a 2.5-cm (1-in.) thick aluminum honeycomb core
surrounded by carbon fiber face sheet plies. The emissivity of the payload fairing is approximately 0.9. The fairing
thermal insulation, which is attached to the outside of the fairing composite, is sized such that the composite never
exceeds the Bounding Fairing Composite Temperature profile shown in Figure 4 - 18. The curve is truncated at 240
seconds, although the approximate time of payload fairing jettison for a GTO mission from Cape Canaveral is typically
earlier, at around 210 seconds into flight. Payload fairing jettison timing is determined by customer requirements and
physical limitations of the system.

The payload fairing will nominally be deployed when free molecular aero-thermal heating is less than 1,135 W/m^2. Other
fairing deployment constraints can be accommodated as a standard service, although they may modestly reduce vehicle
performance. Please contact SpaceX regarding mission-unique fairing deployment requirements.

### 80

### 100

### 120

### 140

### 160

### 180

### 200

### 0 50 100 150 200 250

```
Temperature [F]
```
```
Time [s]
```
**Bounding Fairing Composite Temperature**


Prior to launch, SpaceX requires that customers verify the compatibility of their systems with the Falcon vehicles’
maximum expected flight environments. SpaceX initiates this process by providing the applicable environments. The
customer then summarizes its approach to environmental compatibility verification, and the process concludes with the
customer providing test data to SpaceX, if necessary (Table 7 - 2 ).

Table 4 - 18 summarizes the typical verification activities performed by the customer and provides test levels based
largely on Section 4.3 of this guide. Mission-unique limit levels and coupled loads analysis levels will be developed during
the mission integration process and will serve as the basis for the verification activities. Alternate verification approaches
may be acceptable, but coordination with SpaceX is required.

```
Environment Verification Activities and Test Levels
Quasi-Static Loads
(Section 4.3.1)
```
```
Qualification: Limit levels x 1.25
Protoqualification: Limit levels x 1.25
Acceptance: Limit levels x 1.0
Sine Vibration
(Section 4.3.2)
```
```
Qualification: Limit levels x 1.25, two octave/minute sweep rate
Protoqualification: Limit levels x 1.25, two octave/minute sweep rate
Acceptance: Limit levels x 1.0, four octave/minute sweep rate
Acoustic, Shock, and
Random Vibration
(Section 4.3.3 –
4.3.5)
```
```
Customers shall provide details and justification showing compatibility of spacecraft
hardware to acoustic, shock, and random vibration environments presented herein. SpaceX
does not have specific requirements on spacecraft test margins; however, SpaceX generally
recommends the following standards as references when developing spacecraft/component
test campaigns: GEVS (GSFC-STD-7000), SMC-S-016, or NASA-STD-7001A. Test campaigns
that do not align with methodologies presented in the above standards should have sufficient
accompanying justification. SpaceX can aid in evaluation of these environments if requested
Electromagnetic
(Section 4.3.6)
```
```
SpaceX standard service includes an electromagnetic compatibility assessment.
SpaceX recommends electromagnetic interference/compatibility testing be conducted for
RF-sensitive payloads and may request insight into relevant testing performed
Pressure
(Section 4.3.7)
```
```
SpaceX recommends venting analyses be conducted and may request insight into relevant
analyses performed
Thermal
(Section 4.3.8)
```
```
SpaceX recommends thermal cycle and thermal vacuum testing be conducted and may
request insight into relevant testing performed
```

The standard mechanical interface between SpaceX-provided Falcon launch vehicle hardware and customer-provided
hardware is a 1, 575 - mm (62.01 in.) diameter bolted interface, at the forward end of the launch vehicle PAF. This interface
is designed to conform to the EELV 1 , 575 - mm (62.01 in.) diameter medium payload class mechanical interface defined
in the EELV Standard Interface Specification Rev. C June 2017 , and is defined in Figure 12 - 1 in Appendix A. The forward
end of the 1, 575 - mm PAF includes a close-out plate that isolates the payload from the upper stage of the launch vehicle.
The corresponding keep-out volume is defined Figure 12 - 2 in Appendix A.

SpaceX also offers a 2, 624 - mm (103.307 in.) bolted interface, with an interface plane as defined in Figure 12 - 3. The
close-out structure protrudes above the 2, 624 - mm plane, and the resulting keep-pout volume is defined in Figure 12 - 4.
SpaceX can provide a structural riser as a nonstandard service to raise the height of the payload interface plane above
the keep-out volume. Please contact SpaceX for details.

For customers with 937-mm or 1, 194 - mm or 1,666 mm (36.89 in. or 47.01 in. or 65.59 in.) clampband interface
requirements, SpaceX will either provide and integrate a payload adapter and clampband separation system or will
integrate an adapter and separation system chosen and provided by the customer with the launch vehicle, as a standard
service. For customers with alternative interface requirements, SpaceX can procure almost any industry-standard
adapter system as a nonstandard service. SpaceX has experience integrating numerous commercially available and
internally developed adapters and separation systems. Falcon 9 and Falcon Heavy are compatible with adapter and
separation system products offered by RUAG, CASA, Planetary Systems Corporation and other industry-leading
providers.

The standard SpaceX Falcon fairing is 5.2 m ( 17 .2 ft) in outer diameter and 13. 2 m (4 3. 5 ft) high overall. Fairing structures
and dynamics result in a payload static envelope^3 as defined in Figure 12 - 5 in Appendix A.

The base of the payload static envelope is defined at the local payload region 0 station. Both the 1, 575 - mm and the
2 , 624 - mm interface planes are below station 0. The interface plane offsets are defined for both PAFs in Figure 12 - 2 and
Figure 12 - 4 in Appendix A. Any payload adapters required (e.g., to achieve a 937-mm or 1, 194 - mm or 1, 666 - mm (36.89
in. or 47.01 or 65.59 in.) interface) will utilize a portion of the payload static envelope and the PAF standard envelope.

The geometry of the PAF allows for payload hardware to protrude below the base of the payload static envelope. These
additional payload lower volumes are shown in Figure 12 - 6 and Figure 12 - 7 (for the 1, 575 - mm PAF), and Figure 12 - 8 and
Figure 12 - 9 (for the 2, 624 - mm PAF).

The standard fairing includes one access door in the cylindrical portion; SpaceX can also provide a fairing with up to
eight access doors as a nonstandard service. The payload fairing doors are all in fixed positions and circular, with a 610 -
mm ( 24 - in.) diameter size.

All processing requiring access to the payload must be completed prior to fairing encapsulation, including standard
remove/install-before-flight items. Post-encapsulation access via the fairing door(s) for remove/install-before-flight

(^3) Payload static envelope indicates the volume that the spacecraft is allowed to occupy under static conditions, and
accounts for payload dynamic deflections relative to the fairing as detailed in Figure 12 - 5 , without intrusion by the fairing
due to its dynamic motions. Dynamic deflections are verified via coupled loads analysis.


items that cannot be accomplished prior to encapsulation can be provided as a nonstandard service. In the event of a
payload anomaly requiring customer access to the payload, the standard concept of operations for Falcon vehicles is to
return the launch vehicle to the hangar and remove the fairing. Access doors are not designed for emergency access
into the payload fairing after encapsulation or once the launch vehicle is on the pad.

A single internal fairing RF antenna system can be provided as a nonstandard service for use during payload antenna
testing while on the launch pad, using common command and telemetry frequencies. For missions using an internal
fairing RF antenna, SpaceX utilizes fixed RF antennae locations on the fairing and will work to clock the payload
accordingly. Contact SpaceX for further information on multiple RF antennae systems or nonstandard frequencies.
Internal fairing RF antenna systems are not available for using during flight.

SpaceX can also provide a break wire signal to inform the spacecraft when the fairing is jettisoned, as a nonstandard
service, to be used for enabling spacecraft transmitter activation on a non-interference basis.

SpaceX can also provide an extended fairing as a nonstandard service. The extended fairing has the same diameter as
the standard faring (5.2 m, 17.2 ft) and an overall height of 18.7 m (61.25 ft). The dimensions of the payload static
envelope are denoted in Figure 12 - 10 in Appendix A. Most of the standard and non-standard services provided for the
standard fairing are available for the extended fairing as well. Please contact SpaceX for more details.

Falcon vehicles provide electrical connectivity between the payload and customer-provided electrical ground support
equipment (EGSE) prior to launch, as well as in-flight separation device commanding and separation monitoring. Falcon
launch vehicles do not provide either payload command or interleaved telemetry access during flight as a standard
service.

As a standard service, Falcon launch vehicles provide two in-flight disconnect electrical interface points located at the
payload separation plane. Connector locations and pin designation will be determined during the mission integration
process. SpaceX will supply 37- or 61-pin electrical connectors and will provide the payload-side connector halves to the
customer. Alternatively, the customer can supply mission-unique electrical connectors and provide the launch vehicle-
side connector halves to SpaceX.

The Falcon 9 and Falcon Heavy systems accommodate electrical connectivity between customer EGSE and the payload
during most processing and integration activities. Table 5 - 1 summarizes the availability of interfaces during standard
processing and integration activities. Customers may connect directly between their EGSE and their payload during
payload processing operations. Electrical interfaces will not be available during SpaceX adapter mate, encapsulation,
launch vehicle integration and rollout operations. However, between these steps the customer will be able to interface
with its payload. Customers may supply separate EGSE for payload processing facility (PPF) and pad operations or may
relocate EGSE from the PPF to the pad.

```
Phase Interface Connection
In PPF (payload processing) Customer cables directly to payload
In PPF (adapter mate and encapsulation) None – SpaceX is connecting the payload to the flight adapter harness;
SpaceX will provide payload to PAF connection cables
In PPF (encapsulated) Customer cables to PPF junction box or equivalent interface
Transport to hangar None – mobile
In hangar (pre-integration) Customer cables to hangar junction box
In hangar (launch vehicle integration) None – SpaceX is connecting the flight adapter harness to the second
stage flight harness
```

```
In hangar (on transporter-erector) Customer cables to hangar junction box
Rollout None – mobile
On pad (horizontal and vertical) 6.1-m (20-ft) customer cables (provided by customer) to pad junction
box
Flight None – separation indication only
```
Pad EGSE provided by the customer will be housed in an instrument bay beneath the launch pad deck (Section 6.1).
Payload EGSE is connected to a SpaceX-provided junction box. The payload customer typically provides 6.1-m ( 20 - ft)
cables to connect the payload EGSE to the junction box.

The junction box is connected to the launch vehicle transporter-erector via a ground harness. A harness then runs along
the length of the transporter-erector and connects to the second-stage T+0 quick-disconnect. The flight side of the
second-stage quick-disconnect mates to up to four dedicated payload electrical harnesses that are provided by SpaceX
as part of the second stage. The payload harnesses are routed along the exterior of the second-stage propellant tanks,
underneath raceway covers that provide protection during ground and flight operations. At the top of the second stage
the harnesses are routed through the PAF (Section 5.1.1) and to the spacecraft separation plane.

The total cable lengths between the payload racks/EGSE and the spacecraft separation plane are listed in Table 5 - 2 and
shown in Figure 5 - 1.

```
Launch Site PPF Hangar Launch Pad
VSFB (SLC-4) 30.5 m (100 ft) 208.5 m (684 ft) 171.9 m (564 ft)
CCSFS (SLC-40) 18.3 m (60 ft) 197.8 m (649 ft) 171.9 m (564 ft)
KSC (LC-39A) 18.3 m (60 ft) 181.1 m (594 ft) 196.3 m (644 ft)
```

Separation device commands are used to initiate spacecraft separation from the second stage. Falcon launch vehicles
can provide up to 36 separation device commands, typically implemented as up to 1 8 redundant commands. Up to 96
additional (48 redundant) commands can be accommodated as a nonstandard service; please contact SpaceX for
details.

Falcon vehicles are capable of detecting six separation events through breakwire pairs, and a separation indication signal
for each will be included in launch vehicle telemetry. Additional breakwire sensing may be available; contact SpaceX for
more information. SpaceX requires that at least one circuit on each spacecraft electrical connector be looped back on
the spacecraft side for breakwire indication of spacecraft separation within launch vehicle telemetry. Customers may
request that any number of circuits on the spacecraft electrical connectors be looped back on the launch vehicle side
for breakwire indication of spacecraft separation within spacecraft telemetry.

SpaceX can supply inter-range instrumentation group IRIG-B000 or IRIG-B120 time from its GPS clocks to customer
EGSE at the PPF and/or the launch pad. A launch countdown clock can also be supplied in the IRIG CS-5246 format.
These timing services are provided as a standard service; other options are available as nonstandard services.


SpaceX requires that customers verify the compatibility of their systems with the Falcon mechanical and electrical
interfaces before shipment to the launch site. As a standard service, SpaceX will support a payload adapter mechanical
fit check, including electrical connector location compatibility, at a facility of the customer’s choosing. This interface
compatibility verification does not include a shock test. Second-unit and later flights of similar systems may be subject
to reduced pre-ship verification requirements. Nonstandard verification approaches can be developed on a mission-
unique basis.


SpaceX operates a Falcon launch site at Space Launch Complex 40 (SLC-40) at Cape Canaveral Space Force Station
(CCSFS), Florida. SLC-40 was previously used by the US Air Force for Titan III and Titan IV launches, and it has been
extensively modified by SpaceX to accommodate the Falcon family of launch vehicles.

The SLC-40 launch pad is located at 28 ̊ 33.72’ (28.5620°) N latitude, 80 ̊ 34.630’ (80.5772°) W longitude. Launch
azimuths from SLC-40 support low- to mid-inclination LEO, high-inclination LEO orbits including polar orbits and SSO,
GTO and Earth escape orbits (Section 3.1).

SpaceX facilities at SLC- 40 (Figure 6 - 1 ) include a launch vehicle integration hangar, propellant and pressurant storage
and supply areas, a launch pad, and lightning towers. A SpaceX administrative facility is located adjacent to the launch
complex.

SpaceX provides the use of an off-pad PPF as a standard service for CCSFS launch operations. CCSFS processing and
launch operations, including PPF services, are described in Section 8.

In April 2014, SpaceX signed a 20-year lease with NASA for use of historic Launch Complex 39A (LC-39A) at John F.
Kennedy Space Center (KSC), located on Merritt Island off the central Florida coast. NASA constructed LC-39A (Figure
6 - 2 ) in the early 1960s to conduct missions under the legendary Apollo program and, later, with the space shuttle. After
facility upgrades in 2016, SpaceX completed its first LC-39A launch on February 19, 2017, with the Falcon 9 transport of
CRS-10, as part of an ISS commercial resupply mission. SpaceX has continued the pad’s legacy, launching Falcon 9
from LC-39A twelve times in 2017 alone and Falcon Heavy in February 2018 for its demonstration mission.


The LC-39A launch pad is located at 28.6082° N latitude, 80.6041° W longitude. Launch azimuths from LC-39A support
low- to mid-inclination LEO, GTO and Earth escape orbits (Section 3.1).

LC-39A includes an existing launch pad. The site’s design mirrors the facilities and operations at SpaceX’s other launch
pads and leverages lessons learned. Located 8 miles from the main KSC gate, the launch complex at LC-39A (Figure 6 - 2 )
is the largest location that SpaceX has activated for launch operations since the company’s inception in 2002.

The LC-39A hangar has been designed to receive, integrate and roll out Falcon 9 and Falcon Heavy launch vehicles
(Figure 6 - 2 ). With 55,000 sq ft of floor space and 34,000 sq ft of high bay, the hangar contains 90-ton, 50-ton and 30-ton
bridge cranes as well as integration rails, electrical support equipment and GN2, GHe and other supplies for performing
launch vehicle processing and integration with the encapsulated payload.

Based on a survey of the route, the maximum incline that the integrated launch vehicle experiences during transportation
is 2.9 degrees and occurs as it is moved up to the pad.

CCSFS is a US Space Force Range with controlled access. SpaceX will facilitate pre-approval, badging and access for
customer personnel requiring access to CCSFS. Once badged, customer personnel will have access to the appropriate
areas of the launch base. Non-US persons are subject to additional pre-approval and escort requirements, which will be
facilitated by SpaceX.

Customers typically fly commercial transport to Orlando International Airport, rent cars at the airport, and find lodging
between Titusville and Cocoa Beach for the duration of their stay in Florida. Customer personnel who are US persons
may use their own rental cars for on-base transportation. The area offers a full range of services; your mission manager
can provide you with additional detailed recommendations. SpaceX does not provide transportation or lodging for
customer personnel during CCSFS launch campaigns.


As a standard service, SpaceX provides desk and office space for customer personnel at CCSFS in Hangar AO (Figure
6 - 3 ).

These facilities are available from customer arrival through launch + 3 days. Offices are provided with US-standard power
(120V, 60 Hz), high-speed Internet service and standard office equipment. The pad customer room is located in a bunker
below the launch pad and is used during pad operations.

The SpaceX Launch Control for SpaceX flights is located just outside the south entrance to CCSFS, providing easy
access to all customers. These facilities are equipped with fiber-optic connections to the launch site and a connection


into the launch site’s main data system, allowing easy data transfers between the control facility, the pad and the range,
along with required external users and agencies. A customer room that can accommodate eight people is provided
within the facility for customer technical management personnel.

SpaceX operates a Falcon launch site at Space Launch Complex 4 East (SLC-4E) at Vandenberg Space Force Base
(VSFB), California (Figure 6 - 5 ). SLC-4E was also previously used by the US Air Force for Titan III and Titan IV launches,
and it has been extensively modified by SpaceX to accommodate Falcon launch vehicles. The facilities include the PPF,
vehicle integration hangar, customer office area, pad customer room, launch pad, and launch and landing control. The
PPF is attached to the north side of the vehicle integration hangar as shown in Figure 6 - 5. The two facilities share a
common door through which an encapsulated payload will pass for integration to the launch vehicle. The customer
office area is within walking distance of the PPF and is available to support customer administrative needs. There are
multiple offices and conference rooms available in the building and sections of the building can be closed off as
necessary to separate working areas between organizations. The pad customer room is located next to the launch pad
and equipped to support customer EGSE racks and work stations during payload processing at the pad. The Launch and
Landing Control (Bldg 8505) is located on the North Base and is equipped to support customer EGSE racks and
workstations for day-of-launch activities.

The SLC-4E launch pad is located at 34 ̊ 37.92’ (34.6320°) N latitude, 120 ̊ 36.64’ (120.6107°) W longitude. Launch
azimuths from SLC-4E support high-inclination LEO orbits, including polar orbits and SSO (Section 3.1). SLC-4E
processing and launch operations are described in Section 8.


VSFB is a US Space Force base with controlled access. SpaceX will facilitate pre-approval, badging and access for
customer personnel requiring access to VSFB. Once badged, customer personnel will have access to the appropriate
areas of the launch base. Non-US persons are subject to additional pre-approval and escort requirements, which will be
facilitated by SpaceX.

Customers typically fly commercial transport to Los Angeles International Airport (LAX), rent cars at the airport, and find
lodging between Lompoc and Santa Maria for the duration of their stay in California. The drive between LAX and VSFB
takes approximately 3 hours. Customers occasionally fly into Santa Barbara Airport (SBA) as well; the drive from SBA to
VSFB takes about an hour. Customer personnel who are US persons may use their own rental cars for on-base
transportation. SpaceX does not provide transportation or lodging for customer personnel during VSFB launch
campaigns. The area offers a full range of services; your mission manager can provide you with additional detailed
recommendations.

As a standard service, SpaceX provides desk and office space (Figure 6 - 6 ) for customer personnel. These facilities are
available from customer arrival through launch + 3 days. Offices are provided with US-standard power (120 V, 60 Hz),
high-speed Internet service and standard office equipment.

The pad customer room is located in a bunker below the launch pad and is used during pad operations. Figure 6 - 7 below
shows the size and layout of this facility.


The SpaceX Launch Control is located approximately 11 miles north of the pad. These facilities are equipped with fiber-
optic connections to the launch site and a connection into the launch site’s main data system, allowing easy data
transfers between the control facility, the pad and the range, along with required external users and agencies. A customer
room is provided within the facility and can accommodate up to 12 customer technical personnel.


SpaceX headquarters (Figure 6 - 9 ) are conveniently located in Hawthorne, CA, a few miles inland from Los Angeles
International Airport. The design and manufacturing facility spans more than 1.5 million sq ft and ranks among the
largest manufacturing facilities in California; two complete Falcon 9s can fit end-to-end along the short length of the
building. Facilities include multiple Falcon 9 and Falcon Heavy manufacturing stations, fairing production and integration
stations, nine stations for final assembly of the Merlin engine, and Dragon spacecraft production areas.

Structural and propulsion testing are performed at the SpaceX Rocket Development Facility in McGregor, Texas (Figure
6 - 10 ). Conveniently located two hours from both Austin and Dallas, the site is staffed with test engineers, technicians
and management personnel.

SpaceX’s government outreach and licensing team is located in Washington, DC.


Falcon launch services are available via direct contract with SpaceX and through certain managed procurement services.
To begin your direct contract relationship with SpaceX, please contact the SpaceX Sales department. The Sales
department will work with you to develop a launch services contract.

To streamline communication and ensure customer satisfaction, SpaceX provides each Falcon launch services
customer with a single technical point of contact from contract award through launch (Figure 7 - 1 ). Your mission
manager will be responsible for coordinating mission integration analysis and documentation deliverables, planning
integration meetings and reports, conducting mission-unique design reviews (as required) and coordinating all
integration and test activities associated with the mission. The mission manager also coordinates all aspects of launch
vehicle production, range and range safety integration, and all mission-required licensing leading up to the launch
campaign. The mission manager works closely with the customer, SpaceX technical execution staff and all associated
licensing agencies in order to achieve a successful mission.

The mission manager will work with the customer to create a spacecraft-to-launch vehicle interface control document
(ICD)—the master document for a Falcon launch vehicle mission. Following signature approval of the ICD, SpaceX
maintains configuration control of the document.

```
Build & Flight
Reliability
```
```
Customer Ops &
Integration
```
```
Avionics
```
```
Customer Program
Manager Mission Manager SpaceXLeadership
```
```
Production &
Launch
```
```
Vehicle
Engineering
```
```
Propulsion
Engineering
```
```
Customer/Satellite Teams
```
```
Range Safety
```
### FAA

```
Customer Organization External Organizations
```

Once the payload arrives at the launch site, physical accommodation of customer hardware and associated ground
support equipment is managed by the payload integration manager—part of the launch operations team. However, the
mission manager continues to be the customer’s primary SpaceX point of contact at the launch site and coordinates all
launch site activities to ensure customer satisfaction during this critical phase.

As part of any Falcon launch service, SpaceX will:

```
 Provide personnel, services, hardware, equipment, documentation, analyses and facilities to support mission
planning, launch vehicle production and acceptance, payload integration, and launch.
 Secure required launch licensing, including Federal Aviation Administration (FAA) and State Department
licenses, with input from the payload customer. (Note: Customers are responsible for any launch licenses
specific to payload operation).
 Secure third-party liability insurance for the launch (Note: Customer retains responsibility for satellite
insurance at all times).
 Provide all range and safety documents for the payload provider to complete (per AFSPCMAN 91- 710 and 14
CFR Part 400).
 Facilitate the range and range safety integration process.
 Provide up to three sets of 37- or 61-pin satellite-to-launch vehicle in-flight disconnect electrical connectors,
or integrate customer-provided mission-unique connectors.
 Provide a 1, 575 - mm bolted interface compatible with the 62.01-in. diameter Medium Payload Class
mechanical interface defined in the EELV Standard Interface Specification, or a 2, 624 - mm bolted interface as
defined in section 5.1.1.
 Provide one 937-mm or 1, 194 - mm or 1, 666 - mm (36.89-in. or 47.01-in. or 65.59-in.) adapter and low-shock
clampband separation system, or integrate a customer-provided mission-unique separation system.
 Provide an adapter and technical support for a mechanical interface compatibility verification test at a facility
of the customer’s choosing.
 Provide transportation for the customer’s spacecraft container and all ground support equipment (GSE) from
the launch site landing location to the spacecraft processing location, if necessary.
 Provide ISO Class 8 (Class 100,000 cleanroom) integration space for the payload and GSE prior to the
scheduled launch date, including facilities and support to customer’s hazardous operations.
 Provide certified mechanical GSE to support physical mating of the payload to the payload adapter, perform
fairing encapsulation, and integrate the encapsulated system with the launch vehicle.
 Process the launch vehicle, integrate and encapsulate the payload within the fairing, and test electrical
interfaces with the payload.
 Provide conditioned air into the fairing during encapsulated ground processing.
 Provide one payload access door in the fairing, located at a fixed pre-defined location.
 Conduct a countdown dress rehearsal for customer launch team members supported by SpaceX Mission
Management.
 Launch the payload into the specified orbit within the specified environmental constraints.
```

```
 Perform 3 - axis attitude control or spin-stabilized spacecraft separation.
 Perform a collision avoidance maneuver (as required).
 Verify spacecraft separation from the launch vehicle and provide an orbit injection report.
 Deliver a final post-flight report, which will include payload separation confirmation, ephemeris, payload
environment, significant events and any mission-impacting anomalies.
```
A detailed statement of work and deliverables list, including these standard services, will be developed during contract
negotiation.

Table 7 - 1 provides a standard launch integration schedule, starting at contract signature and proceeding through the
post-flight summary. A detailed schedule, including required customer deliverables, is developed during contract
negotiation.

```
Estimated Schedule Title Purpose
L-24 months Contract signature Provides authority to proceed with work
L-22 months
Mission integration kickoff
Presents the project schedule, a summary of
mission requirements and proposed preliminary
design solutions for any mission-unique
requirements
L-12 months
Completion of mission
integration analyses
```
```
Delivers all mission-unique design and analysis
results to the Customer and prepares the ICD for
signature in advance of this milestone
L- 3 months Launch campaign readiness
review
```
```
Verifies that all people, parts and paper are ready
for the shipment of the payload to the launch site
and are ready to begin launch site activities
L-2 days Launch readiness review
Verifies readiness to proceed with the countdown
and launch, including launch range and FAA
concurrence (conducted two days prior to launch)
Separation + TBD^ minutes Orbit injection report
Delivers best-estimate state vector, attitude, and
attitude rate based on initial data
Launch + 8 weeks Flight report Reports the flight, environments, separation state,
and a description of all mission-impacting
anomalies and progress on their resolution
```
Table 7 - 2 and Table 7 - 3 provide an overview of standard documentation and information required from the customer.
Note: these lists are not all-inclusive but, rather, represent minimum requirements. Depending on the specific payload,
additional customer requirements may apply.


Customer Deliverables Description
Payload safety data Provides detailed payload information to support SpaceX generation of range safety
submittals, requirements tailoring and launch operations planning. Includes hazard
analyses and reports, vehicle break-up models and detailed design/test information
Finite-element and CAD
models

Used in coupled loads analyses and compatibility assessments. Specific format and other
requirements are supplied during the mission integration process
Environment analysis
inputs

Payload inputs for SpaceX environment analyses. Includes payload thermal model and
others, as required
Inputs to ICD Describes all mission-specific requirements. SpaceX generates and controls the ICD, but
input is required from the customer. ICD compliance information is required prior to
launch
Environmental test
statement and data

Defines the payload provider’s approach to qualification and acceptance testing, including
general test philosophy, testing to be performed, objectives, test configuration, methods
and schedule. Actual test procedures are not required. Specific qualification and
acceptance test data may be required prior to launch to demonstrate compatibility with
the SpaceX launch service
Launch site operations
plans and procedures

Describes all aspects of mission activities to be performed at the launch site. Operating
procedures must be submitted for all operations that are accomplished at the launch site.
Hazardous procedures must be approved by Range Safety
Mission data Information in support of reviews is required throughout the mission integration process

Customer Deliverables Description
FAA payload
determination
information

Non-US government payloads must be reviewed by the FAA to determine whether their
launch would jeopardize public safety and other US interests (Title 14 CFR part 415
subpart D). Payload providers may need to provide additional information to enable
SpaceX to submit an application for review
Launch site visitor
information

To obtain the appropriate permissions, SpaceX requires information for non-US customer
personnel prior to visiting the launch site
Launch site GSE details Details on GSE that a non-US customer plans to bring to the launch site are required for
import/export compliance


Falcon launch vehicle operations are described in this section for launches from CCSFS and KSC (Section 6.1) and VSFB
(Section 6.1.2). SpaceX launch operations are designed for rapid response (targeting less than one hour from vehicle
rollout from the hangar to launch). Customers are strongly encouraged to develop launch readiness capabilities and
timelines consistent with a rapid prelaunch concept of operations.

The Falcon launch vehicle system and associated operations have been designed for minimal complexity and minimal
time at the pad (Figure 8 - 1 ). Customer payload processing is performed in a PPF. After completion of standalone
spacecraft operations (typically over a 20-day period) by L-10 days, SpaceX performs the adapter mate and fairing
encapsulation at the PPF. The spacecraft is then transported to the integration hangar. The launch vehicle is processed
in the integration hangar at the launch complex and then loaded on the transporter-erector. The encapsulated assembly
is mated to the launch vehicle at approximately L-5 days, followed by end-to-end system checkouts. Falcon 9 and Falcon
Heavy systems are designed for rollout and launch on the same day, but SpaceX can perform an earlier rollout and
conduct a longer countdown if required.

For standard service processing and integration, payloads should be delivered to the launch site four weeks prior to
launch. Alternative delivery schedules can be arranged as a nonstandard service.

Customers typically deliver their payloads via air or ground transport. Cape Canaveral offers two convenient landing
locations for customers delivering their payloads and associated equipment via air transport: the Shuttle Landing Facility
and the CCSFS Skid Strip. Vandenberg provides one landing location at the VSFB airfield, approximately 14 miles north
of the launch complex. Non-US payloads coming to VSFB via the airfield must clear customs at LAX or another port of
entry prior to arrival at VSFB.

As a standard service, SpaceX will arrange for the customer’s spacecraft container and all associated test and support
equipment to be offloaded from the plane and transported to the payload processing facility. Ground transport services
can also be provided by AstroTech Space Operations or Spaceport Systems International; SpaceX can facilitate these
as a nonstandard service.


SpaceX provides an ISO Class 8 (Class 100,000) PPF for processing customer spacecraft, including equipment
unloading, unpacking/packing, final assembly, nonhazardous flight preparations, and payload checkout. The PPF is
available to customers from four weeks prior to launch, with 16 hours per day standard availability and access during
that period. Additional time in the payload processing facility may be available as a nonstandard service. The PPF layouts
for VSFB and CCSFS are shown in Figure 8 - 2 , Figure 8 - 3 , and Figure 8 - 4 respectively.


Services and equipment provided for satellite processing within the PPF are outlined in Table 8 - 1. Additional space is
provided for customer GSE and operations personnel. A facility HVAC system maintains PPF environments. SpaceX will
continuously monitor relative humidity, temperature and cleanliness in the PPF using particle counters. Cleanliness
monitoring using witness plates is available as a nonstandard service. After encapsulation and prior to launch vehicle
mate, SpaceX will verify purge media source and ducting cleanliness. The customer must supply any necessary cables
and converters for its GSE to interface with PPF power. SpaceX can supply alternative power sources as a nonstandard
service.

The PPF is also designed to accommodate hazardous operations such as hypergolic propellant loading and ordnance
installation. Any required fueling operations will be performed by customer personnel with assistance from SpaceX
personnel. All personnel must use certified SCAPE suits, pass a physical and attend SCAPE training classes.

All spacecraft processing operations within the PPF must be completed by L-10 days to allow for mating to the payload
adapter, fairing encapsulation and transportation to the launch vehicle integration hangar in preparation for launch.

### CCSFS VSFB

Clean Room

Dimensions

```
No less than 9.1 m x 9.1 m ( 30 ft x 30 ft) of
dedicated spacecraft processing floor
space, including for payload fueling
operations.
```
```
No less than 29.2 m x 20.7 m floor size
(95.8 ft x 67.9 ft)
```
Exterior door No less than ( 34 ft x 18 ft 11 in10.36) m high x 5.^76 m wide No less than 6.01 m high x 6.01 m wide (20 ft x 20 ft)

Temp/Clean See See


### CCSFS VSFB

```
Table 4 - 2 (PPF facility HVAC) Table 4 - 2 (PPF facility HVAC)
```
Overhead Crane
Quantity 2 2
Hook height 18 m (59 ft) 18.3 m (60 ft)

Capacity
Crane 1: 27,215 kg (30 ton)
Crane 2: 13,607 kg (15 ton)
both certified for hypergolic lifting

```
North Crane: 27,215 kg (30 T)
South Crane: 18,143 kg (20 T)
```
Hoist Speed (min/max) 6.1 cm/609 min (0.2 ft /20 min), per c^ rane 6.1 cm/609 min (0.2 ft/20 min), per crane^

Operation modes Independent Independent or synchronized
Access Equipment

(^45) hardware, ladders, movable platforms-ft boom lifts, pallet jack, lifting Pallet jack, lifting hardware, ladders, movable platforms
Electrical
60 Hz AC 120V 1480V 3--phase, 120/208V 3phase service - phase, and 120V 1service- phase and 120/208V 3-phase^
50 Hz AC 220/380V UPS back up–^ WYE, 3 - Phase, 5-Wire with 220/380VUPS backup-^ WYE, 3 - Phase, 4-Wire with
Grounding Per MIL-STD- 1542 Per MIL-STD- 1542
GN 2 Supply
Quality MIL-PRF-27401, Grade B MIL-PRF-27401, Grade B
Pressure 34,473 kPa (5,000 psi) 34,473 kPa (5,000 psi)
Flow rate 1 ,699.2 Nm^3 /hr (1,000 scfm) 1 ,699.2 Nm^3 /hr (1,000 scfm)
Helium Supply
Quality MIL-PRF-27407, Grade A MIL-PRF-27407B, Type 1, Grade B
Pressure 39,300 kPa (5,700 psi) 41,368 kPa (6,000 psi)
Flow rate 1 ,699.2 Nm^3 /hr (1,000 scfm) 1 ,699.2 Nm^3 /hr (1,000 scfm)
Compressed Air Supply
Pressure 758 kPa (110 psi) 862 kPa (125 psi)
Communications
Administrative phone VOIP phones VOIP phones
Paging system Yes Yes
Area warning system Yes Yes
Security
Locking facility Yes Yes
Launch site badges Yes Yes
Video monitoring Yes Yes
As an alternative nonstandard service, SpaceX can arrange the use of commercial processing facilities near CCSFS or
VSFB for payload processing. If a payload is processed at a facility other than the SpaceX-provided PPF, SpaceX can
provide environmentally controlled transportation from that facility to the launch vehicle integration hangar.
Joint operations begin ten days before launch. Payload attachment to the PAF and fairing encapsulation are performed
by SpaceX within the payload processing facility (Figure 8 - 5 ). Fairing encapsulation is performed in the vertical
orientation. Transportation is performed in the vertical orientation, and environmental control is provided throughout the


transportation activity. Once at the launch vehicle integration hangar, the encapsulated assembly is rotated to horizontal
and mated with the launch vehicle already positioned on its transporter-erector.

Once the encapsulated assembly is mated to the launch vehicle, the hangar facility HVAC system is connected via a
fairing air conditioning duct to maintain environmental control inside the fairing. The payload is then reconnected to
EGSE (if required) and electrical interfaces are verified. At this point, the integrated launch vehicle is ready for rollout and
launch (Figure 8 - 6 ).


The main decision-making roles and responsibilities for launch operations are shown in Table 8 - 2. Note that this list is
not inclusive of all stations participating in the launch, but, rather, is limited to those that have direct input in the decision-
making process.

```
Position Abbrev. Organization
Chief Engineer CE SpaceX
Mission Manager MM SpaceX
Launch Director LD SpaceX
Missile Flight Control Officer, or
Flight Safety Officer
```
```
MFCO, or
FSO Launch Range^
Operations Safety Manager, or
Ground Safety Officer
```
```
OSM, or
GSO Launch Range^
```
The launch control organization and its lines of decision-making are shown in Figure 8 - 7. The details of the launch control
organization are somewhat dependent on the mission and customer. The payload manager, or a payload manager
representative, will sit at the payload station in the SpaceX launch control center alongside the SpaceX mission manager.

SpaceX provides a spacecraft control center for remote payload command and control operations during the launch
countdown. Customer EGSE and spacecraft personnel will be located within the spacecraft control center during launch.
The spacecraft control center includes full fiber-optic voice, video and Internet connectivity to the launch site, SpaceX
Launch Control (Section 8.5.3), and other range facilities.

```
Launch Decision
Author ity
```
```
Oper ations Safety
Launch Dir ector Manager
```
```
Fl ight
Ter mination
System
```
```
Gr ound
```
```
Avionics Pr opul sion
```
```
Fl ight
Softwar e
```
```
GNC
```
```
Gr ound
Contr ol l er
```
```
Vehicl e
Contr ol l er
```
```
Launch
Softwar e
```
```
Range Customer
Launch
Dir ector
```
```
Launch
Contr ol
```
```
Range
Coor dinator
```
```
Mission
Manager
```
```
Chief
Engineer
```

The SpaceX console design is modular, expandable and completely modern (Figure 8 - 8 ). SpaceX uses standard
computer and display systems with software designed for industrial system control. Consoles also include voice
communications capabilities, including voice nets, voice-over Internet protocol (IP) integration with remote sites, and IP
phones. Video viewing and control are provided using the video-over-IP systems.

After readiness is verified, the integrated Falcon vehicle may be rolled out from the hangar to the pad on its transporter-
erector (Figure 8 - 9 ). Once the vehicle is at the pad, the payload air conditioning system is reconnected, which helps
maintain environmental control through liftoff. Electrical connectivity is provided via ground cables (Section 5.2.1). The
vehicle will typically be erected only once, although the capability exists to easily return it to a horizontal orientation if
necessary.

Customer access to the payload while the vehicle is outside of the hangar requires special accommodations and is a
nonstandard service. Payload access is not available while the launch vehicle is vertical.


Falcon launch vehicles are designed to support a countdown duration as short as one hour. Early in the countdown, the
vehicle performs LOX, RP-1 and pressurant loading, and it executes a series of vehicle and range checkouts. The
transporter-erector strongback is retracted just prior to launch. Automated software sequencers control all critical
Falcon vehicle functions during terminal countdown. Final launch activities include verifying flight termination system
status, transferring to internal power, and activating the transmitters. Engine ignition occurs shortly before liftoff, while
the vehicle is held down at the base via hydraulic clamps. The flight computer evaluates engine ignition and full-power
performance during the prelaunch hold-down, and if nominal criteria are satisfied, the hydraulic release system is
activated at T-0. A safe shutdown is executed should any off-nominal condition be detected.

Falcon launch vehicle systems and operations have been designed to enable recycle operations when appropriate.
Although every recycle event and launch window requirement is unique, Falcon vehicles offer the general capability to
perform multiple recycles within a given launch window, eliminating unnecessary launch delays.

In the event of a launch scrub, the transporter-erector and launch vehicle will stay vertical. Remaining on the pad provides
uninterrupted payload-to-EGSE connectivity through the T-0 umbilical, eliminating the need to relocate EGSE from the
instrumentation bay to the hangar after a scrub. However, for any long-duration launch postponements, SpaceX will
return the vehicle on the transporter-erector to the hangar.

First-stage powered flight lasts approximately three minutes, with commanded shutdown of the nine first-stage engines
based on remaining propellant levels. The second stage burns an additional five to six minutes to reach initial orbit, with
deployment of the fairing typically taking place early in second-stage powered flight. Subsequent operations are unique
to each mission but may include multiple coast-and-restart phases as well as multiple spacecraft separation events.

After reaching the spacecraft injection orbit and attitude, the Falcon vehicle issues a spacecraft separation command,
providing the electrical impulses necessary to initiate spacecraft separation. Indication of separation is available in
second-stage telemetry.

If a contamination and collision avoidance maneuver is necessary, the second stage performs the maneuver shortly
after separation. A contamination and collision avoidance maneuver is provided as a standard service for individual
primary payloads. For multi-manifested and secondary payloads, please contact SpaceX regarding collision avoidance
requirements.

SpaceX will provide a quick-look orbit injection report to the customer shortly after spacecraft separation, including a
best-estimate spacecraft separation state vector. A final, detailed post-flight report is provided within eight weeks of
launch.

SpaceX makes every effort to mitigate space debris by responsibly passivating and disposing of hardware on orbit.
Customer-specific requirements on disposal may impose modest reductions to the performance specifications
indicated in Section 3.2.


Sample mission profiles for Falcon 9 and Falcon Heavy are shown in Figure 8 - 10 and Figure 8 - 11 , and sample Falcon 9 timelines for a GTO mission and LEO mission
are shown in Table 8 - 3 and Table 8 - 4. Note: each flight profile is unique and will differ from these examples.



Mission Elapsed Time Event

T - 3 s Engine start sequence
T + 0 Liftoff
T + 74 s Maximum dynamic pressure (max Q)
T + 147 s Main engine cutoff (MECO)
T + 151 s Stage separation
T + 158 s Second engine start-1 (SES-1)
T + 222 s Fairing deploy
T + 484 s Second engine cutoff 1 (SECO-1)
T + 1636 s Second engine start-2 (SES-2)
T + 1696 s Second engine cutoff-2 (SECO-2)
T + 1996 s Spacecraft separation

Mission Elapsed Time Event

T – 3 s Engine start sequence
T + 0 Liftoff
T + 67 s Maximum dynamic pressure (max Q)
T + 145 s Main engine cutoff (MECO)
T + 148 s Stage separation
T + 156 s Second-engine start-1 (SES-1)
T + 195 s Fairing deploy
T + 514 s Second-engine cutoff-1 (SECO-1)
T + 3086 s Second engine start-2 (SES-2)
T + 3090 s Second engine cutoff-2 (SECO-2)
T + 3390 s Spacecraft separation


Falcon customers are required to meet AFSPCMAN 91-710 Range User's Manual and FAA 14 CFR Part 400 requirements
in the design and operation of their flight and ground systems. These requirements encompass mechanical design,
electrical design, fluid and pressurant systems, lifting and handling systems, ordnance and RF systems, GSE, and other
design and operational features. SpaceX will serve as the safety liaison between the customer and the range.

Most ranges consider hazardous systems and operations to include ordnance operations, pressurized systems that
operate below a 4-to-1 safety factor, lifting operations, operations or systems that include toxic or hazardous materials,
high-power RF systems and laser systems, and a variety of other systems and operations. The details of the system
design and its operation will determine whether the system or related operations are considered hazardous. Typically,
additional precautions are required for operating systems that are considered hazardous, such as redundant valving
between pressurant and propellant. Additional precautions will be determined during the safety approval process with
SpaceX and the launch range. All hazardous operations require procedures that are approved by both SpaceX and the
launch range prior to execution. Ordnance operations, in particular, require coordination to provide reduced RF
environments, cleared areas, safety support and other requirements.

For systems or operations that do not meet safety requirements but are believed to be acceptable for ground operations
and launch, a waiver is typically produced for approval by the launch range safety authority. Waivers require considerable
coordination and are considered a last resort; they should not be considered a standard practice.


If you are considering SpaceX launch services, please contact the SpaceX Sales department:

```
SpaceX
Attention: Sales
Rocket Rd.
Hawthorne, CA 90250
sales@spacex.com
```

Figure 1-1: SpaceX vehicles are designed for high cross-platform commonality ................................ 2

Figure 2-1: Falcon 9 overview ......................................................................................................................... 6

Figure 2-2: The Falcon Heavy demonstration mission launched from KSC on February 6, 2018 .... 7

Figure 2-3: Falcon Heavy first-stage engine layout .................................................................................... 8

Figure 2-4: Falcon vehicle coordinate frame ............................................................................................ 10

Figure 3-1: SpaceX 1,575-mm payload attach fitting .............................................................................. 12

Figure 3-2: SpaceX 2,624-mm payload attach fitting .............................................................................. 12

Figure 3-3: Allowable center-of-gravity height above the 1,575-mm plane ........................................ 13

Figure 3-4: Allowable center-of-gravity height above the 2,624-mm plane ........................................ 13

Figure 4-1: Falcon 9 and Falcon Heavy flight limit load factors for “standard” mass payloads (over

4,000 lb) ........................................................................................................................................................... 17

Figure 4-2: Falcon 9 flight limit load factors for light mass payloads (under 4,000 lb) .................... 18

Figure 4-3: Maximum limit level axial equivalent sine environment for Falcon 9 and Falcon Heavy

........................................................................................................................................................................... 19

Figure 4-4: Maximum limit level lateral equivalent sine environment for Falcon 9 and Falcon Heavy

........................................................................................................................................................................... 19

Figure 4-5: Falcon 9 maximum predicted acoustic environment (P95/50), 60% fill-factor, 131.3 dB

OASPL (Cape Canaveral) and 131.4 dB OASPL (Vandenberg) in third octave, with fairing acoustic

blankets ............................................................................................................................................................ 20

Figure 4-6: Falcon 9 maximum predicted acoustic environment (P95/50), 60% fill-factor, 131.4 dB

OASPL (Cape Canaveral) and 131.6 OASPL (Vandenberg) in full octave, with fairing acoustic

blankets ............................................................................................................................................................ 22

Figure 4-7: Falcon 9 maximum predicted acoustic environment (P95/50), 60% fill-factor, 137.6 dB

OASPL (Cape Canaveral) and 137.9 dB OASPL (Vandenberg) in third octave, without fairing

acoustic blankets ........................................................................................................................................... 23

Figure 4-8: Falcon 9 maximum predicted acoustic environment (P95/50), 60% fill-factor, 137.6 dB

OASPL (Cape Canaveral) and 137.9 dB OASPL (Vandenberg) in full octave, without fairing acoustic

blankets ............................................................................................................................................................ 25

Figure 4-9: Falcon Heavy maximum predicted acoustic environment (P95/50), 60% fill-factor, 135.2

dB OASPL (third octave) ............................................................................................................................... 26

Figure 4-10: Falcon Heavy maximum predicted acoustic environment (P95/50), 60% fill-factor,

135.6 dB OASPL (full octave) ....................................................................................................................... 28

Figure 4-11: Falcon 9/Heavy random vibration maximum predicted environment (P95/50) at top

of PAF [5.13 grms] ......................................................................................................................................... 30

Figure 4-12: Falcon 9/Heavy frequency bin breakdown ......................................................................... 31

Figure 4-13: Falcon 9 worst-case radiated environment ........................................................................ 33


Figure 4- 1 4: Falcon Heavy worst-case radiated environment .............................................................. 34

Figure 4-15: Maximum spacecraft emissions .......................................................................................... 35

Figure 4-16: Fairing avionics emissions envelope ................................................................................... 36

Figure 4-17: Launch site emissions ............................................................................................................ 37

Figure 4-18: Maximum payload fairing spot temperature seen by payload ....................................... 38

Figure 5-1: On-pad electrical interfaces ..................................................................................................... 43

Figure 6-1: Space Launch Complex 40 at Cape Canaveral Space Force Station, Florida ............... 45

Figure 6-2: LC-39A at Kennedy Space Center, Florida ............................................................................ 46

Figure 6-3: Hangar AO ................................................................................................................................... 47

Figure 6 - 4: Layout of customer office space in Hangar AO ................................................................... 47

Figure 6-5: Space Launch Complex 4 East at Vandenberg Space Force Base, California .............. 48

Figure 6-6: Vandenberg customer office space layout ........................................................................... 49

Figure 6-7: Pad customer room .................................................................................................................. 50

Figure 6-8: Customer control rooms at SpaceX Launch Control .......................................................... 50

Figure 6-9: SpaceX’s headquarters in Hawthorne, California ................................................................ 51

Figure 6-10: SpaceX Texas test facility and test operations ................................................................. 51

Figure 7-1: Mission management organization ....................................................................................... 52

Figure 8-1: Illustrative Falcon launch vehicle processing, integration and launch operations

schedule ........................................................................................................................................................... 56

Figure 8-2: VSFB PPF and integration hangar layout .............................................................................. 57

Figure 8-3: CCSFS PPF East Bay floor plan .............................................................................................. 57

Figure 8-4: CCSFS PPF West Bay floor plan ............................................................................................. 58

Figure 8-5: Payload encapsulation and integration sequence .............................................................. 60

Figure 8-6: Integrated Falcon 9 on the transporter-erector within the integration hangar and rolling

out ..................................................................................................................................................................... 60

Figure 8-7: Launch control organization .................................................................................................... 61

Figure 8-8: SpaceX launch control at CCSFS (left) and VSFB (right) ................................................... 62

Figure 8-9: Launch vehicle rollout and erection ....................................................................................... 62

Figure 8-10: Falcon 9 sample mission profile .......................................................................................... 64

Figure 8-11: Falcon Heavy sample mission profile ................................................................................. 65

Figure 12-1: 1,575-mm interface drawing (interface plane details) ..................................................... 75

Figure 12-2: 1,575-mm interface drawing (close-out offset and keep-out volume) .......................... 76

Figure 12-3: 2,624-mm interface drawing (interface plane details) ..................................................... 77

Figure 12-4: 2,624-mm interface drawing (close-out offset and keep-out volume) .......................... 78

Figure 12-5: Payload static envelope (standard Falcon fairing) ........................................................... 79

Figure 12-6: Payload lower volume, with 1,575-mm PAF (1 of 2) ......................................................... 80

Figure 12-7: Payload lower volume, with 1,575-mm PAF (2 of 2) ......................................................... 81

Figure 12-8: Payload lower volume, with 2,624-mm PAF (1 of 2) ......................................................... 82


Figure 12-9: Payload lower volume, with 2,624-mm PAF (2 of 2) ......................................................... 83

Figure 12-10: Falcon extended fairing with payload static envelope ................................................... 84

Table 1-1: Key safety features of Falcon launch vehicles ......................................................................... 3

Table 2-1: Falcon dimensions and characteristics ..................................................................................... 9

Table 3-1: Falcon 9 and Falcon Heavy launch services .......................................................................... 11

Table 4-1: Recommended quasi-static load factors for transportation .............................................. 15

Table 4-2: Temperature and cleanliness environments ......................................................................... 15

Table 4-3: Falcon 9 maximum predicted acoustic environment (P95/50), 60% fill-factor, with fairing

acoustic blankets ........................................................................................................................................... 21

Table 4-4: Falcon 9 maximum predicted acoustic environment (P95/50), 60% fill-factor, with fairing

acoustic blankets ........................................................................................................................................... 22

Table 4-5: Falcon 9 maximum predicted acoustic environment (P95/50), 60% fill-factor, without

fairing acoustic blankets .............................................................................................................................. 24

Table 4-6: Falcon 9 maximum predicted acoustic environment (P95/50), 60% fill-factor, without

fairing acoustic blankets .............................................................................................................................. 25

Table 4-7: Falcon Heavy maximum predicted acoustic environment (P95/50), 60% fill-factor, 135.2

dB OASPL (third octave) ............................................................................................................................... 27

Table 4-8: Falcon Heavy maximum predicted acoustic environment (P95/50), 60% fill-factor, 135.6

dB OASPL (full octave) .................................................................................................................................. 28

Table 4-9: Payload adapter-induced shock at the spacecraft separation plane (P95/50) .............. 29

Table 4-10: Falcon 9/Heavy random vibration maximum predicted environment (P95/50) at top of

PAF [5.13 grms] .............................................................................................................................................. 30

Table 4-11: Falcon 9 RF systems characteristics ................................................................................... 32

Table 4-12: Falcon Heavy RF systems characteristics .......................................................................... 32

Table 4-13: Falcon 9 worst-case radiated environment ......................................................................... 33

Table 4-14: Falcon Heavy worst-case radiated environment ................................................................ 34

Table 4-15: Maximum spacecraft emissions ........................................................................................... 35

Table 4-16: Fairing avionics emissions envelope .................................................................................... 36

Table 4-17: Launch site emissions ............................................................................................................. 37

Table 4-18: Spacecraft environmental compatibility verification example ........................................ 39

Table 5-1: Payload electrical interface connectivity ................................................................................ 41

Table 5-2: Maximum expected cable lengths between payload racks/EGSE and the separation

plane ................................................................................................................................................................. 42

Table 7-1: Standard launch integration schedule .................................................................................... 54

Table 7-2: Required documents and data for all payloads .................................................................... 55


Table 7-3: Additional required documents and data for non-US persons and non-US government

payloads ........................................................................................................................................................... 55

Table 8-1: Services and equipment for payload processing .................................................................. 58

Table 8-2: Launch control organization ..................................................................................................... 61

Table 8-3: Falcon 9 sample flight timeline—GTO mission ..................................................................... 66

Table 8-4: Falcon 9 sample flight timeline—LEO mission ...................................................................... 66

ACS ..................................................................................................................................................................... attitude control system

AFSPCMAN .................................................................................................................................. Air Force Space Command Manual

AWG ........................................................................................................................................................................ American wire gauge

BPSK ................................................................................................................................................................ binary phase shift keying

C3 .............................................................................................................................................. characteristic energy (escape energy)

CAD ..................................................................................................................................................................... computer-aided design

CCSFS ....................................................................................................................................... Cape Canaveral Space Force Station

CRS ....................................................................................................................................................... Commercial Resupply Services

DSSS ................................................................................................................................................ direct-sequence spread spectrum

EELV ................................................................................................................................................ evolved expendable launch vehicle

EGSE ........................................................................................................................................... electrical ground support equipment

ESPA ................................................................................................................................................. EELV secondary payload adapter

FAA ....................................................................................................................................................... Federal Aviation Administration

FM ......................................................................................................................................................................... frequency modulation

GN 2 ................................................................................................................................................................................. gaseous nitrogen

GPS ............................................................................................................................................................... Global Positioning System

GSE ............................................................................................................................................................... ground support equipment

GSO ........................................................................................................................................................................ geosynchronous orbit

GTO ........................................................................................................................................................ geosynchronous transfer orbit

HEO ........................................................................................................................................................................... highly elliptical orbit

HITL ........................................................................................................................................................................ Hardware-in-the-loop

HVAC ..................................................................................................................................... heating, ventilation and air conditioning

ICD ................................................................................................................................................................ interface control document

IP ..................................................................................................................................................................................... Internet protocol

IRIG .................................................................................................................................................. inter-range instrumentation group

ISS ................................................................................................................................................................ International Space Station


LAX ..................................................................................................................................................... Los Angeles International Airport

LEO ...................................................................................................................................................................................... low Earth orbit

LOX .........................................................................................................................................................................................liquid oxygen

LV ........................................................................................................................................................................................ launch vehicle

LVLH ......................................................................................................................................................... local vertical/local horizontal

M1D................................................................................................................................................................................. Merlin 1D engine

Max Q ....................................................................................................................................................... maximum dynamic pressure

MECO ......................................................................................................................................................................... main engine cut-off

MPE ................................................................................................................................................... maximum predicted environment

MVac .................................................................................................................................................................................. Merlin Vacuum

NASA....................................................................................................................... National Aeronautics and Space Administration

OASPL ....................................................................................................................................................... overall sound pressure level

PAF .......................................................................................................................................................................... payload attach fitting

PCM ..................................................................................................................................................................... pulse code modulation

PPF ................................................................................................................................................................ payload processing facility

PSK .............................................................................................................................................................................. phase shift keying

Q .................................................................................................................................................................................... dynamic pressure

RF ...................................................................................................................................................................................... radio frequency

RP- 1 ................................................................................................................................ rocket propellant-1 (rocket-grade kerosene)

SBA ........................................................................................................................................................................ Santa Barbara Airport

SC ............................................................................................................................................................................................... spacecraft

SCAPE .................................................................................................................. self-contained atmospheric protective ensemble

SECO ...................................................................................................................................................................... second-engine cut-off

SES ............................................................................................................................................................................ second-engine start

SLC ........................................................................................................................................................................ space launch complex

SpaceX .................................................................................................................................... Space Exploration Technologies Corp.

SPL ........................................................................................................................................................................... sound pressure level

SRS ................................................................................................................................................................ shock response spectrum

SSO ...................................................................................................................................................................... sun-synchronous orbit

TE ................................................................................................................................................................................ transporter-erector

TEA-TEB .............................................................................................................................................. triethylaluminum-triethylborane

US .......................................................................................................................................................................................... United States

VSFB ..................................................................................................................................................... Vandenberg Space Force Base


Date Update

Oct 2015 Original Release
May 2016 Minor updates and clarifications
Jan 2019 Falcon 9 Block 5 and Falcon Heavy updates
Apr 2020 Minor environments updates
Aug 2020 Minor administrative updates
August 2021 Minor administrative updates
Added 2, 624 - mm payload attach fitting and 1, 666 - mm payload adapter
Added description of extended fairing
Updated acoustics environment to include levels with no fairing acoustic blankets installed
Added Appendix A with mechanical interface drawings

September 2021 Corrected typo on total Falcon height (ft) with extended fairing in Table 2- 1
Corrected markings on footers on pages 64 through 88













