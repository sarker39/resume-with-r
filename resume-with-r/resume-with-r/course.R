
tibble::tibble(
  ~authors, ~title, ~journal, ~status 
  
)%>% 
  brief_entries(glue::glue("<authors>, \\textbf{<title>}, <journal>, <status>)) 



