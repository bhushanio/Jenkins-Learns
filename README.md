Things I've learned:

📁 Projects
A Jenkins Project is a job configuration that defines what to build, how to build it, and when to build it—like a blueprint for automation.
 ___________________________________________________________________________________________________________________________________________________________________________
| Project Type         | Description                                                                 | Use Case                                                             |
| -------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Freestyle Project    | Basic job with GUI-based configuration.                                     | Simple tasks like running scripts, compiling code, or copying files. |
| Pipeline Project     | Code-based pipeline using a Jenkinsfile. Supports complex workflows.        | CI/CD automation with multiple stages (build, test, deploy).         |
| Multibranch Pipeline | Automatically manages pipelines for each branch in a repository.            | Automate workflows for multiple Git branches (e.g., `dev`, `main`).  |
| Folder               | Organizes multiple jobs into a single group.                                | Managing large Jenkins setups with many jobs or teams.               |
| External Job         | Monitors tasks run outside Jenkins (legacy use).                            | When Jenkins needs to track external job status.                     |
| Matrix Project       | Builds the same project across multiple configurations (OS, versions, etc). | Cross-platform or multi-environment testing.                         |
 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🔁 Triggers
Settings that control when a Jenkins job should start automatically.
 ____________________________________________________________________________________________________________
|   Trigger Name                               |   Use Case                                                  |
| -------------------------------------------- | ----------------------------------------------------------- |
| Trigger builds remotely (e.g., from scripts) | Trigger a build from a shell script or external tool        |
| Build after other projects are built         | Run deployment job after a build or test job                |
| Build periodically                           | Run every night at 2 AM or on a custom schedule             |
| GitHub hook trigger for GITScm polling       | Auto-build when someone pushes code to GitHub               |
| Poll SCM                                     | Check for Git changes every few minutes and build if needed |
 ------------------------------------------------------------------------------------------------------------

⚙️ Build Environment
Configurations that define the context in which your build runs, like variables, secrets, and cleanup actions.
 _____________________________________________________________________________________________________________________________
| **Environment Option**                          | **Use Case**                                                              |
| ----------------------------------------------- | ------------------------------------------------------------------------- |
| **Environment**                                 | Set variables like credentials, paths, or global params for the build     |
| **Delete workspace before build starts**        | Clean up old files to ensure a fresh, clean build environment             |
| **Use secret text(s) or file(s)**               | Inject sensitive info (like passwords or keys) securely into the build    |
| **Add timestamps to the Console Output**        | Add time info to each log line to help with debugging and timing analysis |
| **Inspect build log for published build scans** | Check logs for special markers or metadata from tools like Gradle scans   |
| **Terminate a build if it's stuck**             | Automatically stop a build if it hangs for too long                       |
| **With Ant**                                    | Use Apache Ant build tool for Java or legacy projects                     |
 -----------------------------------------------------------------------------------------------------------------------------

🔨 Build Steps
The core actions Jenkins performs during the build, such as running scripts or compiling code.
 _______________________________________________________________________________________________________________
| **Build Step**                          | **Use Case**                                                        |
| --------------------------------------- | ------------------------------------------------------------------- |
| **Execute shell**                       | Run shell commands/scripts (Linux/macOS) during the build           |
| **Execute Windows batch command**       | Run `.bat` or command-line instructions on Windows during the build |
| **Invoke Ant**                          | Use Apache Ant to build Java or legacy projects                     |
| **Invoke Gradle script**                | Run Gradle build tasks (common for Java/Kotlin projects)            |
| **Invoke top-level Maven targets**      | Run Maven goals (like `clean install`) for Java projects            |
| **Invoke a project using its URL**      | Trigger another Jenkins job using a URL                             |
| **Set build status on GitHub commit**   | Update GitHub with build success/failure status for the commit      |
| **Copy artifacts from another project** | Bring in files (like JARs, logs) from a different Jenkins job       |
| **Publish JUnit test result report**    | Show test results and failures in Jenkins UI after build runs       |
| **Send build artifacts over SSH**       | Deploy or copy build output to a remote server via SSH              |
 ---------------------------------------------------------------------------------------------------------------

✅ Post-Build Actions
Tasks Jenkins performs after the main build, such as sending notifications, archiving artifacts, or triggering other jobs.
 __________________________________________________________________________________________________________________________
| **Post-Build Action**                       | **Use Case**                                                               |
| ------------------------------------------- | -------------------------------------------------------------------------- |
| **Archive the artifacts**                   | Save build output (e.g., JARs, ZIPs, logs) so they can be downloaded later |
| **Publish JUnit test result report**        | Display test results and failures in Jenkins for visibility and tracking   |
| **Email Notification**                      | Send an email when a build succeeds, fails, or changes state               |
| **Editable Email Notification**             | Send a **custom** email with advanced formatting, recipients, and triggers |
| **Build other projects**                    | Automatically trigger other Jenkins jobs after this one finishes           |
| **Deploy artifacts to remote repositories** | Push built files to external storage (e.g., Nexus, Artifactory)            |
| **Send build artifacts over SSH**           | Upload files to a remote server via SSH after the build                    |
| **Record fingerprints of files**            | Track where a file came from and which job created it                      |
| **Slack Notifications** (via plugin)        | Send build status updates to a Slack channel                               |
 --------------------------------------------------------------------------------------------------------------------------
