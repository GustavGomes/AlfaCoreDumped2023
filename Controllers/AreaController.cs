using System.Runtime.CompilerServices;
using AlfaCoreDumped.Domain.Entities.CompanyResources;
using AlfaCoreDumped.Infrastructure.DbRepository;
using Microsoft.AspNetCore.Mvc;

namespace AlfaCoreDumped.Controllers
{
    [ApiController]
    [Route("area")]
    public class AreaController : ControllerBase
    {
        private IAlfaRepository _alfaRepository;
        public AreaController(IAlfaRepository alfaRepository)
        {
            _alfaRepository = alfaRepository;
        }

        [HttpGet("{areaId}")]
        public ActionResult<Area> GetArea(Guid areaId)
        {
            var area = _alfaRepository.GetArea(areaId);
            if (area == null)
            {
                return NotFound();
            }
            return Ok(area);
        }
    }
}