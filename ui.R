shinyUI(fluidPage(
  
#  titlePanel(h1("Time Table Generator-IISER Pune",align='center'),img(src="iiserpune.jpg")),

#------------------- Add Colors using html tags to headers -----------------------------------
  
  titlePanel(title=div(img(src="iiserpune.jpg",height=72,width=80),h1("Time Table Generator"),align='center')),
  sidebarLayout(position = "right",
                sidebarPanel( h2("Available Courses",align='center')),
                mainPanel(h2("Select Courses"),
                # fluidRow(
                #   column(12,h3("Biology",align='center'))
                # ),
                fluidRow(
                  column(12,
                         radioButtons("bio", label = h3("Biology",align='center'),
                                      choices = list("Choice 1" = 1, "Choice 2" = 2,
                                                     "Choice 3" = 3)))
                )
                
                          ))
  
#---Thinking to Implement(Read More)--------------------------
  # navlistPanel(
  #   "Header A",
  #   tabPanel("Component 1"),
  #   tabPanel("Component 2"),
  #   "Header B",
  #   tabPanel("Component 3"),
  #   tabPanel("Component 4"),
  #   "-----",
  #   tabPanel("Component 5")
  # )
  
  )
  )