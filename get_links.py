def get_links(driver):
    td_tags = driver.find_elements_by_tag_name('td')
    links = []
    for td in td_tags:
        try:
            links.append((td.find_element_by_tag_name('a')
                         .get_attribute('href')))
        except:
            continue
    
    return links