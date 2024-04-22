#include <unistd.h>

int main(int argc, char* argv[], char *envp[]) {
	if (argc < 2) return 1;
	return execvp(argv[1], &argv[1]);
}
