#include <iostream>
#include <stdlib.h>
#include <time.h>

#define ITERATIONS 10000000 // 100000000

int waitTimes[5] = {42,10,25,18,33};

float transition[5][5] =
{
	{0.23,0.33,0.52,0.75,1.00},
	{0.12,0.19,0.37,0.79,1.00},
	{0.30,0.38,0.54,0.78,1.00},
	{0.40,0.52,0.67,0.76,1.00},
	{0.09,0.18,0.46,0.57,1.00}
};

class Rider
{
    public:
        int numberOfRides() const { return *numRides; }
        int currentRide() const { return *ride; }
        int returnTime() const { return *time; }
        void goToNextRide();
        Rider();
        ~Rider();
    private:
        int *numRides;
        int *ride;
        int *time;
};
    
void Rider::goToNextRide()
{
    float odds = (float)rand() / (float)RAND_MAX;

    // *numRides++; // increment the number of rides by one

    for (int j=0; j<5; j++)
    {
        if (odds <= transition[*ride][j]) // for the current ride, determine which will be the next ride
        {
            if ( !( *ride == j) ) *time += 5;
            *ride = j; // the rider is now on the new ride
            break; // we've successfully moved, can now leave loop
        }
    }
    *time += waitTimes[*ride];
    

}

Rider::Rider()
{
    numRides = new int(0);
    ride = new int(2);
    time = new int(0);
}

Rider::~Rider()
{
    delete numRides;
    delete ride;
    delete time;
}

int main()
{
	srand ( time(NULL) ); // initialize random seed

	long int timeTotal = 0;

	for (int n=0; n<ITERATIONS; n++)
	{
//debug		std::cout << "I'm in the for loop\n";
		Rider *kid = new Rider;
        // std::cout << "New kid initialized on ride number " << kid->currentRide() << "\n";
		do
		{
//debug			std::cout << "I'm in the While loop\n";
			kid->goToNextRide();
		} while (kid->currentRide() != 2);

		timeTotal += kid->returnTime();

		delete kid;

	}

	std::cout << "The average time is " << (float)timeTotal / (float)ITERATIONS << "\n";

	return 0;
}
