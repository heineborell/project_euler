#include <stdio.h>

int	main(void)
{
	int	i;
	int	nbr;

	nbr = 20;
	while (1)
	{
		i = 2;
		while (i <= 20)
		{	
			if ((nbr % i) != 0)
				break ;
			i++;
		}
		if (i == 21)
		{
			printf("%i\n", nbr);
			return (0);
		}
		nbr += 20;
	}
	return (0);
}
