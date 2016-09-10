from __future__ import print_function
import numpy as np
from heapq import *
import random as rnd
import math
import copy

inf = float('infinity')


class Particle(object):
    def __init__(self, X, V, r, m):
        self.X = X # Position vector.
        self.V = V # Velocity vector.
        self.r = r # Radius of particle disk.
        self.m = m # Particle mass.

    def advance_position(self, dt):
        self.X += self.V*dt


class Wall(object):
    def __init__(self, wall_type):
        self.wall_type = wall_type


class Collision:
    def __init__(self, particle, obj, Xi):
        self.particle = particle
        self.obj = obj
        self.Xi = Xi

    def calculate_velocities(self):
        #print('V_before_hit: ', self.particle.V)       # TODO: remove
        if isinstance(self.obj, Wall):
            if self.obj.wall_type == 'vertical':
                self.particle.V = self.particle.V*(-self.Xi, self.Xi) # Equation (3).
                #print('V_vertical_hit: ', self.particle.V)             # TODO: remove
            else: # Horizontal wall.
                self.particle.V = self.particle.V*(self.Xi, -self.Xi) # Equation (4).
                #print('V_horizontal_hit: ', self.particle.V)           # TODO: remove
        else: # obj is a particle. 
            particle1 = self.particle
            particle2 = self.obj
            dV = particle2.V - particle1.V
            dX = particle2.X - particle1.X
            R = particle1.r + particle2.r
            # Equation (11):
            particle1.V += ((1 + Xi)*(particle2.m/(particle1.m + particle2.m))*(dV.dot(dX)/(R**2)))*dX
            particle2.V -= ((1 + Xi)*(particle1.m/(particle1.m + particle2.m))*(dV.dot(dX)/(R**2)))*dX


class EventDrivenSimulation:
    def __init__(self, particles, Xi):
        self.particles = set(particles) # Numbers of particles.      TODO: rename to initial_particle_configuration or something like that
        self.Xi = Xi # Restitution coefficient.
        self.ensemble = [(0, copy.copy(particles))] # List with particle configurations at given time.
        self.T = 0 # Time

    # Run simulation for N collisons.
    def run(self, N):
        # Initialization:
        collision_events = [] # Priority queue for the collision events.
        self._queue_collisions(collision_events, self.particles)
        
        # Event loop:
        collision_count = 0
        while collision_events and collision_count < N:
            dt, collision = heappop(collision_events)

            # Moving particles forward in time until first collision:
            for p in self.particles:
                p.advance_position(dt)
                self.T += dt

            # Calculating new velocities for particles involved in collision:
            collision.calculate_velocitites()

            # Calculating next collision for particles involved in current collision:
            involved_particles = set([collision.particle])
            if isinstance(collision.obj, Particle):
                current_particles.add(collision.obj)
            self._queue_collisions(collision_events, involved_particles)


    def _queue_collisions(self, queue, particles):
        for pi in particles:
            wall_collision = wall_collision_detection(pi)
            if wall_collision[0] < inf:
                    heappush(collision_events, wall_collision)
            for pj in copy.copy(self.particles).difference(particles): # Ensuring not to calculate any pairs twice or calculating collisions with itself.
                particle_collision = particle_collision_detection(pi, pj)
                if particle_collision[0] < inf:
                    heappush(collision_events, particle_collision)



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
            return (self.T + dt_v, Collision(particle, Wall('vertical'), self.Xi))
        else:
            return (self.T + dt_h, Collision(particle, Wall('horizontal'), self.Xi))

    '''NB! needs clarification on what (dV)**2 means in equation (10), when dV.dot(dV) is used in (7)'''
    def _particle_collision_detection(self, particle1, particle2):
        R = particle1.r + particle2.r
        dX = particle2.X - particle1.X # Equation (8).
        dV = particle2.V - particle1.V # Equation (9).
        d = (dV.dot(dX))**2 - dV.dot(dV)*(dX.dot(dX) - R**2) # Equation (10).

        # Equation (7):
        if dV.dot(dX) >= 0:
            dt = inf
        elif d <= 0:
            dt = inf
        else:
            dt = -(dV.dot(dX) + math.sqrt(d))/(dV.dot(dV))

        return (self.T + dt, Collision(particle1, particle2, self.Xi))



# Runs the test cases from the appendix.
def run_tests():
    global test
    test = True
    # B.1 One particle:
    # A particle hitting a wall should bounce back with the same speed in the opposite direction:
    print('Test 1: ', end = '')
    p = Particle(np.array([0.5, 0.5]), np.array([rnd.uniform(-1.0, 1.0), 0.0]), 0.001, 1.0)
    simulation = EventDrivenSimulation([copy.copy(p)], 1.0, 1)
    simulation.run()
    if (simulation.particles[0].V == -p.V).all():
        print('pass')
    else:
        print('fail')   

    '''
    # A particle hitting a wall at an angle should obey the law of reflection:
    print("Test 2: ", end = '')
    p = Particle(np.array([rnd.random(), rnd.random()]), np.array([rnd.uniform(-1.0, 1.0), rnd.uniform(-1.0, 1.0)]), 0.001, 1.0)
    simulation = EventDrivenSimulation([copy.copy(p)], 1.0, 1)
    simulation.run()
    '''
    
    # A particle with velocity V = (v0, v0), should hit all four walls once before ending up at the same starting point:
    print('Test 3: ', end = '')
    v0 = rnd.uniform(-1.0, 1.0)
    r = 0.001
    p = Particle(np.array([rnd.random(), rnd.random()]), np.array([v0, v0]), r, 1.0)
    simulation = EventDrivenSimulation([copy.copy(p)], 1.0, 4)
    simulation.run()
    test3 = 'pass'
    for pos in simulation.particles[0].position_history:
        #if (pos[0] not in (r, 1-r)) or (pos[1] not in (r, 1-r)): 
        print(pos, (r, 1-r))
        if not (pos == [r, 1-r]).any() or not (pos == (1-r, r)).any():
            test3 = 'fail'
            break
    print(test3)

    
    print(simulation.collision_count)
    
    '''
    # A particle hitting a wall with Xi = 0 should come to a complete stop:
    print('Test 4: ', end = '')
    p = Particle(np.array([rnd.random(), rnd.random()]), np.array([rnd.uniform(-1.0, 1.0), rnd.uniform(-1.0,)]), 0.001, 1.0)
    simulation = EventDrivenSimulation([p], 0.0, 1)
    simulation.run()
    if (p.V == 0).all():
        print('pass')
    else:
        print('fail')
    '''
    # B.2 Two particles:
    # Two particles with m1 = m2, V1 = -V2 hitting each other straight on should have V1' = -V1 and V2' = -V2.




    
def main():
    pass


if __name__ == "__main__":
    run_tests()