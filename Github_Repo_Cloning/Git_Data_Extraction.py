import export as export
import git
repository_url="https://github.com/PhonePe/pulse.git"
destination_directory="/Users/shashankkaundal/Downloads/PhonepePulseData/Gitdataclone"
git.Repo.clone_from(repository_url,destination_directory)