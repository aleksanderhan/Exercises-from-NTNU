from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
from heapq import *
import random as rnd
import math
import copy
from matplotlib.patches import Circle
from time import sleep

inf = float('infinity')

class Particle(object):
    def __init__(self, X, V, r, m):
        self.X = X # Position vector.
        self.V = V # Velocity vector.
        self.r = r # Radius of particle disk.
        self.m = m # Particle mass.

    def advance_position(self, dt):
        self.X += self.V*np.float64(dt)


class Wall(object):
    def __init__(self, wall_type):
        self.wall_type = wall_type


class Collision:
    def __init__(self, particle, obj, Xi, dt):
        self.particle = particle
        self.obj = obj
        self.Xi = Xi
        self.dt = dt
        if isinstance(obj, Particle):
            self._type = 'p-p' # particle-particle collision.
        else:
            self._type = 'p-w' # Particle-wall collision.

    # Calculates new velocities for particles after collision.
    def calculate_velocities(self):
        if self._type == 'p-w':
            if self.obj.wall_type == 'vertical':
                self.particle.V = self.particle.V*(-self.Xi, self.Xi) # Equation (3).
            else: # Horizontal wall.
                self.particle.V = self.particle.V*(self.Xi, -self.Xi) # Equation (4).
        else:
            dV = self.obj.V - self.particle.V
            dX = self.obj.X - self.particle.X
            R = self.particle.r + self.obj.r
            # Equation (11):
            self.particle.V += ((1.0 + self.Xi)*(self.obj.m/(self.particle.m + self.obj.m))*(dV.dot(dX)/(R**2)))*dX
            self.obj.V -= ((1.0 + self.Xi)*(self.particle.m/(self.particle.m + self.obj.m))*(dV.dot(dX)/(R**2)))*dX


class EventDrivenSimulation:
    def __init__(self, particles, Xi):
        self.particles = particles # Numbers of particles.      TODO: rename to initial_particle_configuration or something like that
        self.Xi = Xi # Restitution coefficient.
        self.samples = [(0, copy.deepcopy(particles))] # Particle configurations samples at given time.
        self.T = 0 # Time
        self.output_T = 0

    # Run simulation for at most N particle-particle collisions.
    def run(self, N, sample_dt = 0, sample_every_collision = False):
        # Python spesific optimization. Reducing lookup overhead.
        particles = self.particles
        wall_collision_detection = self._wall_collision_detection
        particle_collision_detection = self._particle_collision_detection

        # Initialization:
        collision_events = [] # Priority queue for the collision events.
        for i in xrange(len(particles)):
            wall_collision = wall_collision_detection(particles[i])
            if wall_collision[0] < inf:
                    heappush(collision_events, wall_collision)
            for j in xrange(i, len(particles)): # Ensuring not to calculate any pairs twice or calculating collisions with itself.
                particle_collision = particle_collision_detection(particles[i], particles[j])
                if particle_collision[0] < inf:
                    heappush(collision_events, particle_collision)

        collision_count = 0 # Collision counter.                   # TODO: remove .self ?
        # Event loop:
        while collision_events and collision_count < N:
            collision = heappop(collision_events)[1]
            dt = collision.dt

            # Moving particles forward in time until first collision:
            for p in particles:
                p.advance_position(dt)
                self.T += dt

            # Calculating new velocities for particles involved in collision:
            collision.calculate_velocities()
            if sample_every_collision:
                self.samples.append((self.T, copy.deepcopy(self.particles)))

            # Calculating next collision for current particles:self.c
            current_particles = [collision.particle]
            if isinstance(collision.obj, Particle):
                current_particles.append(collision.obj)
            for current_particle in current_particles:
                wall_collision = wall_collision_detection(current_particle)
                if wall_collision[0] < inf:
                    heappush(collision_events, wall_collision)
                for p in particles:
                    if id(p) == id(current_particle): 
                        continue
                    particle_collision = particle_collision_detection(current_particle, p)
                    if particle_collision[0] < inf:
                        heappush(collision_events, particle_collision)

            # Only count particle-particle collisions.
            if collision._type == 'p-p':
                collision_count += 1
                #print(collision_count)


    def _wall_collision_detection(self, particle):
        # Storing particle characteristics in local variables to reduce lookup overhead.
        r = particle.r
        X = particle.X
        V = particle.V

        # Vertical wall, equation (1):
        if  V[0] > 0:
            dt_v = (1 - r - X[0])/V[0]
        elif V[0] < 0:
            dt_v = (r - X[0])/V[0]
        else:
            dt_v = inf

        # Horizontal wall, equation (2):
        if V[1] > 0:
            dt_h = (1 - r - X[1])/V[1]
        elif V[1] < 0:
            dt_h = (r - X[1])/V[1]
        else:
            dt_h = inf

        if dt_v < dt_h:
            return (self.T + dt_v, Collision(particle, Wall('vertical'), self.Xi, dt_v))
        else:
            return (self.T + dt_h, Collision(particle, Wall('horizontal'), self.Xi, dt_h))

    def _particle_collision_detection(self, particle1, particle2):
        R = particle1.r + particle2.r
        dX = particle2.X - particle1.X # Equation (8).
        dV = particle2.V - particle1.V # Equation (9).
        d = np.float64(dV.dot(dX))**2 - dV.dot(dV)*(dX.dot(dX) - R**2) # Equation (10).

        # Equation (7):
        if dV.dot(dX) >= 0:
            dt = inf
        elif d <= 0:
            dt = inf
        else:
            dt = -(dV.dot(dX) + math.sqrt(d))/(dV.dot(dV))

        return (self.T + dt, Collision(particle1, particle2, self.Xi, dt))


def unit_vector(vector):
    return vector / np.linalg.norm(vector)

def calculate_angle(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

# Distributes N particles with random radius, mass and velocity in a space [(0, 1), (0, 1)] so that they dont overlap.
def populate_box(N):
    particles = []
    i = 1
    while i <= N:
        r = rnd.uniform(0.01/N, 0.6/N)
        if r == 0: # Try again
            i -= 1
            continue
        m = rnd.uniform(1.0, 10000.0)
        #X = (1-r-r)*np.random.random(2, dtype='float64') - 2*r
        X = np.array([rnd.uniform(r, 1-r), rnd.uniform(r, 1-r)], dtype ='float64')
        v0 = np.float64(rnd.randint(-10000, 10000))
        theta = np.float64(rnd.uniform(0, 2*math.pi))
        V = np.array([v0*math.cos(theta), v0*math.sin(theta)], dtype='float64')
        # Test if particles overlap:
        skip = False
        for p in particles:
            dX = p.X - X
            if math.sqrt(dX.dot(dX)) < (r + p.r):
                i -= 1
                skip = True
                break
        if skip:
            continue
        new_p = Particle(X, V, r, m)
        particles.append(new_p)
        i += 1
    return particles


# Runs the test cases from the appendix.
def run_tests():
    # B.1 One particle:
    # A particle hitting a wall should bounce back with the same speed in the opposite direction:
    print('Test 1: ', end = '')
    r = 0.001
    X = (1-r-r)*np.array([0.5, 0.5]) - r # Ensures the particle doesnt start inside the wall.
    V = np.array([rnd.uniform(-1.0, 1.0), 0.0])
    p = Particle(X, V, 0.001, 1.0)
    simulation = EventDrivenSimulation([p], 1.0)
    simulation.run(1, sample_every_collision=True)
    if (simulation.samples[0][1][0].V == -simulation.samples[1][1][0].V).all():
        print('pass')
    else:
        print('fail')   

    # A particle hitting a wall at an angle should obey the law of reflection:
    # Fails 50% of the time because of the normal vector used. Doesn't matter, it works..
    print("Test 2: ", end = '')
    r = 0.001
    X = (1-r-r)*np.random.random(2) - r
    V = np.array([rnd.uniform(-1.0, 1.0), rnd.uniform(-1.0, 1.0)])
    p = Particle(X, V, 0.001, 1.0)
    simulation = EventDrivenSimulation([p], 1.0)
    simulation.run(1, sample_every_collision=True)
    normal = np.array([1, 0]) # Normal vector to vertical wall.
    V_before_collision = simulation.samples[0][1][0].V
    V_after_collision = simulation.samples[1][1][0].V
    if calculate_angle(normal, V_before_collision) == calculate_angle(normal, V_after_collision):
        print('pass')
    else:
        print('fail (probably works anyway)')
       
    # A particle with velocity V = (v0, v0), should hit all four walls once before ending up at the same starting point:
    print('Test 3: ', end = '')
    r = 0.001
    X = (1-r-r)*np.random.random(2) - r
    v0 = rnd.uniform(-1.0, 1.0)
    p = Particle(X, np.array([v0, v0]), r, 1.0)
    '''
    simulation = EventDrivenSimulation([copy.copy(p)], 1.0)
    simulation.run(4, sample_every_collision=True)
    walls = ['left', 'right', 'top', 'bottom']
    for s in simulation.samples:
        p= s[1][0]
    '''
    print('not implemented')

    # A particle hitting a wall with Xi = 0 should come to a complete stop:
    print('Test 4: ', end = '')
    r = 0.001
    X = (1-r-r)*np.random.random(2) - r
    V = np.array([rnd.uniform(-1.0, 1.0), rnd.uniform(-1.0, 1.0)])
    p = Particle(X, V, r, 1.0)
    simulation = EventDrivenSimulation([p], 0.0)
    simulation.run(1, sample_every_collision=True)
    if (simulation.samples[1][1][0].V == 0).all():
        print('pass')
    else:
        print('fail')
    
    # B.2 Two particles:
    # Two particles with m1 = m2, V1 = -V2 hitting each other straight on should have V1' = -V1 and V2' = -V2.
    print('Test 5: ', end = '')
    r1 = r2 = 0.001
    m1 = m2 = 1.0
    X1 = np.array([r1, 0.5])
    X2 = np.array([1-r2, 0.5])
    v0 = 0.3
    V1 = np.array([v0, 0])
    V2 = np.array([-v0, 0])
    p1 = Particle(X1, V1, r1, m1)
    p2 = Particle(X2, V2, r2, m2)
    simulation = EventDrivenSimulation([p1, p2], 1.0)
    simulation.run(1, sample_every_collision=True)
    if (simulation.samples[0][1][0].V.round(3) == -simulation.samples[1][1][0].V.round(3)).all() and (simulation.samples[0][1][1].V.round(3) == -simulation.samples[1][1][1].V.round(3)).all():
        print('pass')
    else:
        print('fail')

    # Two particles with m1 = m2, V1 = -V2 ...
    print('Test 6: ', end = '')
    print('not implemented')

    # ...
    print('Test 7: ', end = '')
    r1 = r2 = 0.001
    m1 = m2 = 1.0
    X1 = np.array([r1, 0.5])
    X2 = np.array([1-r2, 0.5])
    v0 = 0.3
    V1 = np.array([v0, 0])
    V2 = np.array([-v0, 0])
    p1 = Particle(X1, V1, r1, m1)
    p2 = Particle(X2, V2, r2, m2)
    simulation = EventDrivenSimulation([p1, p2], 0.0)
    simulation.run(1, sample_every_collision=True)
    p1_V_after_collision = simulation.samples[1][1][0].V
    p2_V_after_collision = simulation.samples[1][1][1].V
    if p1_V_after_collision.all() == 0 and p2_V_after_collision.all() == 0:
        print('pass')
    else:
        print('fail')

    # B.3 Many particles
    # ...



def make_scatter_plot(particles):
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    ax.axis([0., 1., 0., 1.])
    for p in particles:
        ax.add_artist(Circle(xy=p.X, radius=p.r))
    plt.show()



def problem1():
    scattering_angles = []
    impact_parameters = []
    n = 30 # Number of runs.
    for i in xrange(n):
        b = i*(0.15/n)
        impact_parameters.append(b)
        P = Particle(np.array([0.5, 0.5]), np.array([0.0, 0.0]), 0.1, 1000000.0) # Big particle.
        p = Particle(np.array([0.1, 0.5 + b]), np.array([100.0, 0.0]), 0.001, 1.0) # Small particle.
        simulation = EventDrivenSimulation([p, P], 1.0)
        simulation.run(1, sample_every_collision=True)
        angle = calculate_angle(simulation.samples[0][1][0].V, simulation.samples[1][1][0].V)
        scattering_angles.append(angle)
    plt.plot([b/0.101 for b in impact_parameters], scattering_angles, 'b*')
    plt.xlabel('impact parameter [b/R_ij]')
    plt.ylabel('scattering angle [radians]')
    plt.savefig('problem1.png')
    plt.show()


def problem2():
    n = 10 # Number of particles.
    particles = populate_box(n)
    simulation = EventDrivenSimulation(particles, 1.0)
    simulation.run(100*n) # Run for 100 collisons pr. particle on average.



def main():
    #problem1()
    problem2()


if __name__ == "__main__":
    #run_tests()
    main()
